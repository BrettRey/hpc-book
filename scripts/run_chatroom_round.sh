#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 2 ]]; then
  cat <<'USAGE'
Usage:
  scripts/run_chatroom_round.sh <chapter-tex-file> <output-dir> [mode]

Modes:
  natural    (default) freewheeling writers' room + separate ballot pass
  structured strict panel format

Examples:
  scripts/run_chatroom_round.sh chapters/chapter05.tex notes/chatroom-runs/ch05-natural
  scripts/run_chatroom_round.sh chapters/chapter05.tex notes/chatroom-runs/ch05-structured structured
USAGE
  exit 1
fi

chapter_file="$1"
output_dir="$2"
mode="${3:-natural}"
chapter_ref="$chapter_file"

if [[ "$mode" == "freewheel" ]]; then
  mode="natural"
fi

if [[ "$mode" != "natural" && "$mode" != "structured" ]]; then
  echo "Unknown mode: $mode (expected: natural|structured)" >&2
  exit 1
fi

if [[ ! -f "$chapter_file" ]]; then
  echo "Chapter file not found: $chapter_file" >&2
  exit 1
fi

mkdir -p "$output_dir"
total_lines=$(wc -l < "$chapter_file")

agents=(
  "Parker"
  "Ephron"
  "Twain"
  "Seinfeld"
  "Adams"
  "Wilde"
  "Wodehouse"
)

persona_brief() {
  case "$1" in
    "Parker")
      printf '%s' "Dry, sharp compression. Prefers one clean sting over ornament."
      ;;
    "Ephron")
      printf '%s' "Observational, humane, urbane. Favors clarity with social texture."
      ;;
    "Twain")
      printf '%s' "Plainspoken and concrete. Skeptical of pretension; prefers grounded punch."
      ;;
    "Seinfeld")
      printf '%s' "Everyday observational comedy. Finds absurdity in ordinary process friction."
      ;;
    "Adams")
      printf '%s' "High-concept absurdity, but only when technically clarifying."
      ;;
    "Wilde")
      printf '%s' "Elegant inversion, epigrammatic cadence, controlled flamboyance."
      ;;
    "Wodehouse")
      printf '%s' "Lightly baroque comic phrasing; maintain readability and avoid over-mannered diction."
      ;;
    *)
      printf '%s' "Technical reviewer."
      ;;
  esac
}

coverage_bounds() {
  local idx="$1"
  local parts="$2"
  local start end
  start=$(( (((idx - 1) * total_lines) / parts) + 1 ))
  end=$(( (idx * total_lines) / parts ))
  printf '%s %s\n' "$start" "$end"
}

shuffle_array() {
  printf '%s\n' "$@" | awk 'BEGIN{srand()} {printf "%.12f\t%s\n", rand(), $0}' | sort -k1,1n | cut -f2-
}

build_conversation_order() {
  local extra_count="${1:-4}"
  local pool=()
  local extra=()
  local agent
  for agent in "${agents[@]}"; do
    pool+=("$agent" "$agent")
  done
  mapfile -t extra < <(shuffle_array "${agents[@]}" | head -n "$extra_count")
  for agent in "${extra[@]}"; do
    pool+=("$agent")
  done
  shuffle_array "${pool[@]}"
}

chapter_map_file="$output_dir/chapter_map.txt"
if ! rg -n '^\\(chapter|section|subsection)|^\\textsc\{Definiteness thread\}' "$chapter_file" > "$chapter_map_file"; then
  nl -ba "$chapter_file" | sed -n '1,80p' > "$chapter_map_file"
fi

combined_turns_file="$output_dir/combined_turns.md"

if [[ "$mode" == "structured" ]]; then
  cat > "$combined_turns_file" <<'EOF'
### [R1-M00] Moderator
Moderator: Structured panel mode.
EOF

  mapfile -t structured_speakers < <(printf '%s\n' "${agents[@]}")
  for i in $(seq 1 ${#structured_speakers[@]}); do
    turn_id=$(printf "R1-S%02d" "$i")
    agent="${structured_speakers[$((i - 1))]}"
    persona="$(persona_brief "$agent")"
    prompt_file="$output_dir/${turn_id}-${agent}.prompt.txt"
    turn_file="$output_dir/${turn_id}-${agent}.md"

    read -r cover_start cover_end < <(coverage_bounds "$i" "${#structured_speakers[@]}")
    turn_excerpt_file="$output_dir/${turn_id}-${agent}.excerpt.txt"
    nl -ba "$chapter_file" | sed -n "${cover_start},${cover_end}p" > "$turn_excerpt_file"

    cat > "$prompt_file" <<EOF
You are one reviewer in structured panel mode.

Identity:
- Name: ${agent}
- Persona: ${persona}

Output format (exact):
### [${turn_id}] ${agent}
Keep: <one thing>
Change: <one change>
Risk: <one risk>
Pitch:
- <line with placement ref like ${chapter_ref}:123 — candidate line>

Assigned coverage excerpt:
$(cat "$turn_excerpt_file")

Transcript so far:
$(cat "$combined_turns_file")
EOF

    codex exec --sandbox read-only --cd "$PWD" --output-last-message "$turn_file" < "$prompt_file" >/dev/null
    cat "$turn_file" >> "$combined_turns_file"
    printf '\n\n' >> "$combined_turns_file"
  done

  echo "Wrote turns to: $combined_turns_file"
  exit 0
fi

mapfile -t convo_speakers < <(build_conversation_order 4)
mapfile -t punch_speakers < <(shuffle_array "${agents[@]}")
mapfile -t ballot_speakers < <(shuffle_array "${agents[@]}")
convo_turns="${#convo_speakers[@]}"

{
  echo "### [R1-M00] Moderator"
  echo "Moderator: Open floor. Jump in naturally; do not dominate the room."
  echo "Moderator: Tough-room rule: material first, weak lines are killable."
  echo "Moderator: Conversation pass has ${convo_turns} turns and covers the whole chapter."
  echo "Moderator: Then one punch-up lap and a separate ballot pass."
  echo "Conversation order this run: ${convo_speakers[*]}"
  echo "Punch-up order this run: ${punch_speakers[*]}"
  echo "Ballot order this run: ${ballot_speakers[*]}"
  echo
} > "$combined_turns_file"

for i in $(seq 1 "$convo_turns"); do
  turn_id=$(printf "R1-T%02d" "$i")
  agent="${convo_speakers[$((i - 1))]}"
  persona="$(persona_brief "$agent")"
  prompt_file="$output_dir/${turn_id}-${agent}.prompt.txt"
  turn_file="$output_dir/${turn_id}-${agent}.md"

  read -r cover_start cover_end < <(coverage_bounds "$i" "$convo_turns")
  turn_excerpt_file="$output_dir/${turn_id}-${agent}.excerpt.txt"
  nl -ba "$chapter_file" | sed -n "${cover_start},${cover_end}p" > "$turn_excerpt_file"

  cat > "$prompt_file" <<EOF
You are one writer in a live comedy writers' room revising a chapter.

Room norms:
- Sound like a person in a room, not a review template.
- React to prior turns organically; short digressions are fine.
- Keep this contribution to 2-6 sentences before line proposals.
- Avoid repeating scaffold patterns (for example, "yes on X, no on Y" every turn).
- Humor should clarify, not derail.
- Land 1-2 concrete candidate lines with placement refs.
- At least one candidate must target this focus window: ${chapter_ref}:${cover_start}-${cover_end}

Identity:
- Name: ${agent}
- Persona: ${persona}

Output format (exact):
### [${turn_id}] ${agent}
${agent}: <natural room contribution>
Line candidates:
- <placement ref like ${chapter_ref}:123 — proposed line>
- <optional second line or n/a>

Chapter map:
$(cat "$chapter_map_file")

Focus excerpt:
$(cat "$turn_excerpt_file")

Transcript so far:
$(cat "$combined_turns_file")
EOF

  codex exec --sandbox read-only --cd "$PWD" --output-last-message "$turn_file" < "$prompt_file" >/dev/null
  cat "$turn_file" >> "$combined_turns_file"
  printf '\n\n' >> "$combined_turns_file"
done

{
  echo "### [R1-M01] Moderator"
  echo "Moderator: Punch-up lap. One quick follow-up each. Keep it conversational."
  echo
} >> "$combined_turns_file"

for i in $(seq 1 ${#punch_speakers[@]}); do
  turn_id=$(printf "R1-P%02d" "$i")
  agent="${punch_speakers[$((i - 1))]}"
  persona="$(persona_brief "$agent")"
  prompt_file="$output_dir/${turn_id}-${agent}.prompt.txt"
  turn_file="$output_dir/${turn_id}-${agent}.md"

  cat > "$prompt_file" <<EOF
You are one writer in the punch-up lap of a live room.

Room norms:
- Keep the voice natural; this should read like conversation.
- Keep it tight: 1-4 sentences plus one rewritten line.
- Prefer upgrading an existing candidate line or a weak transition.

Identity:
- Name: ${agent}
- Persona: ${persona}

Output format (exact):
### [${turn_id}] ${agent}
${agent}: <brief natural follow-up>
Punch-up:
- <placement ref like ${chapter_ref}:123 — rewritten line>

Chapter map:
$(cat "$chapter_map_file")

Transcript so far:
$(cat "$combined_turns_file")
EOF

  codex exec --sandbox read-only --cd "$PWD" --output-last-message "$turn_file" < "$prompt_file" >/dev/null
  cat "$turn_file" >> "$combined_turns_file"
  printf '\n\n' >> "$combined_turns_file"
done

{
  echo "### [R1-M02] Moderator"
  echo "Moderator: Ballot pass. Each writer names two keeps and one cut."
  echo
} >> "$combined_turns_file"

for i in $(seq 1 ${#ballot_speakers[@]}); do
  turn_id=$(printf "R1-B%02d" "$i")
  agent="${ballot_speakers[$((i - 1))]}"
  prompt_file="$output_dir/${turn_id}-${agent}.prompt.txt"
  turn_file="$output_dir/${turn_id}-${agent}.md"

  cat > "$prompt_file" <<EOF
You are casting a short ballot after a writers' room pass.

Rules:
- Pick exactly two line refs to keep from earlier proposals.
- Pick exactly one line ref to cut, or n/a.
- Use refs only (no prose after refs).

Output format (exact):
### [${turn_id}] ${agent}
Keep:
- <line ref like ${chapter_ref}:123>
- <line ref like ${chapter_ref}:234>
Cut:
- <line ref from earlier proposals or n/a>

Transcript so far:
$(cat "$combined_turns_file")
EOF

  codex exec --sandbox read-only --cd "$PWD" --output-last-message "$turn_file" < "$prompt_file" >/dev/null
  cat "$turn_file" >> "$combined_turns_file"
  printf '\n\n' >> "$combined_turns_file"
done

ballot_tally_file="$output_dir/ballot_tally.tsv"
awk '
  /^### \[R1-B[0-9][0-9]\]/ {in_ballot=1; section=""; next}
  /^### \[/ {if (!match($0, /^### \[R1-B/)) {in_ballot=0; section=""}}
  in_ballot && /^Keep:/ {section="keep"; next}
  in_ballot && /^Cut:/ {section="cut"; next}
  in_ballot && /^- / {
    ref=$0
    sub(/^- /, "", ref)
    gsub(/[` ]/, "", ref)
    if (ref == "" || ref == "n/a") next
    if (section == "keep") keep[ref]++
    if (section == "cut") cut[ref]++
  }
  END {
    for (k in keep) printf("%s\t%d\t%d\n", k, keep[k], (k in cut ? cut[k] : 0))
    for (k in cut) if (!(k in keep)) printf("%s\t0\t%d\n", k, cut[k])
  }
' "$combined_turns_file" > "$ballot_tally_file"

{
  echo "### [R1-M03] Moderator"
  echo "Moderator: Ballot tally (keep/cut):"
  if [[ -s "$ballot_tally_file" ]]; then
    sort -t $'\t' -k2,2nr -k3,3n "$ballot_tally_file" | while IFS=$'\t' read -r ref keep_count cut_count; do
      echo "- ${ref} : keep ${keep_count}, cut ${cut_count}"
    done
  else
    echo "- none"
  fi

  echo "Moderator: Survivors (keep >= 2 and keep > cut):"
  survivors="$(awk -F'\t' '$2 >= 2 && $2 > $3 {print "- " $1}' "$ballot_tally_file" | sort)"
  if [[ -n "$survivors" ]]; then
    printf '%s\n' "$survivors"
  else
    echo "- none"
  fi
} >> "$combined_turns_file"

echo "Wrote turns to: $combined_turns_file"
