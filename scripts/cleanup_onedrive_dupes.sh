#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Remove OneDrive-style duplicate files ("* 2.*") when they are exact byte copies.

Usage:
  scripts/cleanup_onedrive_dupes.sh [--dry-run] [--verbose]

Options:
  --dry-run, -n   Show what would be removed without deleting files
  --verbose, -v   Also print skipped files (missing base or content mismatch)
  --help, -h      Show this help
USAGE
}

dry_run=0
verbose=0

for arg in "$@"; do
  case "$arg" in
    --dry-run|-n)
      dry_run=1
      ;;
    --verbose|-v)
      verbose=1
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $arg" >&2
      usage >&2
      exit 2
      ;;
  esac
done

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"
cd "${repo_root}"

total=0
removed=0
skipped_missing=0
skipped_different=0

while IFS= read -r -d '' file; do
  total=$((total + 1))
  base="${file/ 2./.}"

  if [[ ! -f "${base}" ]]; then
    skipped_missing=$((skipped_missing + 1))
    if [[ "${verbose}" -eq 1 ]]; then
      printf 'skip (no base): %s\n' "${file#./}"
    fi
    continue
  fi

  if cmp -s -- "${file}" "${base}"; then
    if [[ "${dry_run}" -eq 1 ]]; then
      printf 'would remove: %s\n' "${file#./}"
    else
      rm -f -- "${file}"
      printf 'removed: %s\n' "${file#./}"
    fi
    removed=$((removed + 1))
  else
    skipped_different=$((skipped_different + 1))
    if [[ "${verbose}" -eq 1 ]]; then
      printf 'skip (different): %s\n' "${file#./}"
    fi
  fi
done < <(find . -type f -name '* 2.*' -print0)

printf '\nSummary:\n'
printf '  matched pattern: %d\n' "${total}"
if [[ "${dry_run}" -eq 1 ]]; then
  printf '  removable exact duplicates: %d\n' "${removed}"
else
  printf '  removed exact duplicates: %d\n' "${removed}"
fi
printf '  skipped (no base file): %d\n' "${skipped_missing}"
printf '  skipped (content differs): %d\n' "${skipped_different}"
