#!/usr/bin/env python3
"""
Verify DOIs in references.bib Section 5 (lines 2917-4420)
"""

import re
import requests
import time
from typing import Dict, List, Tuple

def extract_entries(filepath: str, start_line: int, end_line: int) -> List[Tuple[str, Dict]]:
    """Extract bib entries from specified line range."""
    entries = []
    current_entry = None
    current_key = None
    in_range = False
    line_num = 0

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line_num += 1

            if line_num < start_line:
                continue
            if line_num > end_line:
                break

            # Start of new entry
            if re.match(r'^@\w+\{', line):
                if current_entry:
                    entries.append((current_key, current_entry))

                match = re.match(r'^@\w+\{([^,]+)', line)
                current_key = match.group(1).strip() if match else 'unknown'
                current_entry = {'lines': [line_num], 'doi': None, 'author': None, 'title': None, 'year': None}

            elif current_entry is not None:
                current_entry['lines'].append(line_num)

                # Extract DOI
                doi_match = re.search(r'doi\s*=\s*\{([^}]+)\}', line)
                if doi_match:
                    current_entry['doi'] = doi_match.group(1).strip()

                # Extract author
                author_match = re.search(r'author\s*=\s*\{([^}]+)\}', line)
                if author_match:
                    current_entry['author'] = author_match.group(1).strip()

                # Extract title
                title_match = re.search(r'title\s*=\s*\{([^}]+)\}', line)
                if title_match:
                    current_entry['title'] = title_match.group(1).strip()

                # Extract year
                year_match = re.search(r'year\s*=\s*\{?(\d{4})', line)
                if year_match:
                    current_entry['year'] = year_match.group(1).strip()

    if current_entry:
        entries.append((current_key, current_entry))

    return entries

def verify_doi(doi: str) -> Tuple[bool, str]:
    """Verify a DOI by attempting to resolve it."""
    if not doi:
        return False, "No DOI"

    # Clean DOI
    doi = doi.strip()

    # Try to resolve
    url = f"https://doi.org/{doi}"
    try:
        response = requests.head(url, allow_redirects=True, timeout=10)
        if response.status_code == 200:
            return True, "OK"
        else:
            return False, f"HTTP {response.status_code}"
    except requests.exceptions.Timeout:
        return False, "Timeout"
    except requests.exceptions.RequestException as e:
        return False, f"Error: {str(e)[:50]}"

def main():
    filepath = "/Users/brettreynolds/Documents/LLM-CLI-projects/HPC book/references.bib"
    start_line = 2917
    end_line = 4420

    print(f"Extracting entries from lines {start_line}-{end_line}...")
    entries = extract_entries(filepath, start_line, end_line)
    print(f"Found {len(entries)} entries\n")

    working_dois = []
    broken_dois = []
    missing_dois = []

    for key, entry in entries:
        author = (entry.get('author') or 'Unknown')[:50]
        title = (entry.get('title') or 'Unknown')[:60]
        year = entry.get('year') or 'Unknown'

        if entry['doi']:
            print(f"Checking {key}: {entry['doi']}", end=" ... ")
            is_valid, status = verify_doi(entry['doi'])
            print(status)

            if is_valid:
                working_dois.append(key)
            else:
                broken_dois.append({
                    'key': key,
                    'doi': entry['doi'],
                    'status': status,
                    'author': author,
                    'title': title,
                    'year': year
                })

            # Be nice to DOI servers
            time.sleep(0.5)
        else:
            missing_dois.append({
                'key': key,
                'author': author,
                'title': title,
                'year': year
            })

    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"\nTotal entries: {len(entries)}")
    print(f"Working DOIs: {len(working_dois)}")
    print(f"Broken DOIs: {len(broken_dois)}")
    print(f"Missing DOIs: {len(missing_dois)}")

    if broken_dois:
        print("\n" + "="*80)
        print("BROKEN DOIs")
        print("="*80)
        for entry in broken_dois:
            print(f"\n@{entry['key']}")
            print(f"  Author: {entry['author']}")
            print(f"  Title: {entry['title']}")
            print(f"  Year: {entry['year']}")
            print(f"  DOI: {entry['doi']}")
            print(f"  Status: {entry['status']}")

    if missing_dois:
        print("\n" + "="*80)
        print("MISSING DOIs")
        print("="*80)
        for entry in missing_dois:
            print(f"\n@{entry['key']}")
            print(f"  Author: {entry['author']}")
            print(f"  Title: {entry['title']}")
            print(f"  Year: {entry['year']}")

if __name__ == '__main__':
    main()
