# Agent Chatroom Protocol

This file defines how reviewer agents interact in a shared writers' room thread.

## Default Mode: `natural`

`natural` is the default mode and is designed to sound like a real room, not a review template.

- No fixed speaking order in conversation turns.
- Digressions and phatic comments are allowed.
- The moderator enforces coverage and anti-domination only.
- Concrete, placeable line edits are still required.

## Cast (No Gelman)

Default cast:

- `Parker`
- `Ephron`
- `Twain`
- `Seinfeld`
- `Adams`
- `Wilde`
- `Wodehouse`

## Round Structure (`natural`)

Each round has three passes:

1. **Conversation pass** (`R1-T##`)
   Open-floor sequence with variable speaker repetition.
   Whole chapter is covered by rotating focus windows.
2. **Punch-up pass** (`R1-P##`)
   One short follow-up per writer for rewrites/closers.
3. **Ballot pass** (`R1-B##`)
   Each writer submits `2 keeps + 1 cut`.
   Moderator auto-tallies and marks survivors.

## Guardrails

- Avoid repeated setup/payload clause scaffolds.
- Keep humor usable in serious prose.
- Prefer sharp keep/cut discipline over ornamental riffs.
- If two lines do the same job, keep the cleaner one.

## Turn Formats

Conversation:

```md
### [R1-T03] AgentName
AgentName: <natural room contribution>
Line candidates:
- chapters/chapter05.tex:213 — <line>
- <optional second line or n/a>
```

Punch-up:

```md
### [R1-P03] AgentName
AgentName: <brief follow-up>
Punch-up:
- chapters/chapter05.tex:434 — <line>
```

Ballot:

```md
### [R1-B03] AgentName
Keep:
- chapters/chapter05.tex:184
- chapters/chapter05.tex:434
Cut:
- chapters/chapter05.tex:353
```

## Runner

Use:

```bash
scripts/run_chatroom_round.sh <chapter-tex-file> <output-dir> [mode]
```

Examples:

```bash
scripts/run_chatroom_round.sh chapters/chapter05.tex notes/chatroom-runs/ch05-live-room-v2-2026-02-23 natural
scripts/run_chatroom_round.sh chapters/chapter05.tex notes/chatroom-runs/ch05-structured structured
```

## Latest Run

- Session: Chapter 05 live room v2
- Command: `scripts/run_chatroom_round.sh chapters/chapter05.tex notes/chatroom-runs/ch05-live-room-v2-2026-02-23 natural`
- Transcript: `notes/chatroom-runs/ch05-live-room-v2-2026-02-23/combined_turns.md`
