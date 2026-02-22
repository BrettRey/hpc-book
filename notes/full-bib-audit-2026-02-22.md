# Full Bib Audit (2026-02-22)

## Summary
- Bib sources loaded: 1
- Total entries: 799
- Unique keys: 799
- Total issues: 41
- Errors: 0
- Warnings: 13
- Info: 28

## Bib Sources
- `/Users/brettreynolds/Documents/LLM-CLI-projects/.house-style/references.bib`

## Field Style Snapshot
- Journal fields: `journal`=359, `journaltitle`=5, both=0
- Time fields: `year`=794, `date`=1, both=4
- Place fields: `address`=341, `location`=9, both=0

## Issues By Code
- `duplicate_doi_record`: 8
- `invalid_year_format`: 1
- `missing_required_field`: 4
- `mixed_address_location_style`: 1
- `mixed_journal_field_style`: 1
- `mixed_year_date_style`: 1
- `possible_duplicate_record`: 25

## Issue Details
### `duplicate_doi_record` (8)
- [warning] DOI `10.1007/bf00385837` is shared by multiple keys: Boyd1991HPC, boyd1991, boyd1991realism. key=`Boyd1991HPC;boyd1991;boyd1991realism` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1038/s41583-024-00802-4` is shared by multiple keys: Fedorenko2024a, Fedorenko2024naturalkind. key=`Fedorenko2024a;Fedorenko2024naturalkind` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1515/cogl.2011.006` is shared by multiple keys: Goldberg2011, goldberg2011preemption. key=`Goldberg2011;goldberg2011preemption` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1017/9781009085748` is shared by multiple keys: Huddleston2021, HuddlestonPullumReynolds2022. key=`Huddleston2021;HuddlestonPullumReynolds2022` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1177/0142723719869731` is shared by multiple keys: ambridge2019, ambridge2020radical. key=`ambridge2019;ambridge2020radical` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1016/j.cognition.2015.03.016` is shared by multiple keys: kirby2015, kirby2015compression. key=`kirby2015;kirby2015compression` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1515/9783110852820.302` is shared by multiple keys: link1983, link1983plurals. key=`link1983;link1983plurals` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1007/3-540-48199-0_2` is shared by multiple keys: pullum2001, pullum_scholz2001mtsges. key=`pullum2001;pullum_scholz2001mtsges` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.

### `invalid_year_format` (1)
- [warning] Year has non-standard format `2008--2025`. key=`Davies2008COCA` source=`/Users/brettreynolds/Documents/LLM-CLI-projects/.house-style/references.bib` field=`year`
  Suggestion: Use `year={YYYY}` (or `YYYYa`, `YYYYb`) and put extra text in `note`.

### `missing_required_field` (4)
- [warning] Required field `journal` is missing. key=`GelmanLoken2013` source=`/Users/brettreynolds/Documents/LLM-CLI-projects/.house-style/references.bib` field=`journal`
  Suggestion: Add `journal={...}` (or standardize to `journaltitle`, then normalize style).
- [warning] Required field `school` is missing. key=`baird2001` source=`/Users/brettreynolds/Documents/LLM-CLI-projects/.house-style/references.bib` field=`school`
  Suggestion: Add `school={...}`.
- [warning] Required field `publisher` is missing. key=`bechtel2005explanation` source=`/Users/brettreynolds/Documents/LLM-CLI-projects/.house-style/references.bib` field=`publisher`
  Suggestion: Add `publisher={...}`.
- [warning] Required field `school` is missing. key=`winter2002` source=`/Users/brettreynolds/Documents/LLM-CLI-projects/.house-style/references.bib` field=`school`
  Suggestion: Add `school={...}`.

### `mixed_address_location_style` (1)
- [info] Mixed use of `address` (341) and `location` (9).
  Suggestion: Choose one location field style and normalize.

### `mixed_journal_field_style` (1)
- [info] Mixed use of `journal` (359) and `journaltitle` (5).
  Suggestion: Choose one field style for articles and normalize across the bibliography.

### `mixed_year_date_style` (1)
- [info] Mixed use of `year` (794) and `date` (1).
  Suggestion: Normalize to house style (typically keep `year`, optionally also `date` when needed).

### `possible_duplicate_record` (25)
- [info] Same title+first-author+year signature appears under multiple keys: Boyd1991HPC, boyd1991, boyd1991realism. key=`Boyd1991HPC;boyd1991;boyd1991realism`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Fedorenko2024a, Fedorenko2024naturalkind. key=`Fedorenko2024a;Fedorenko2024naturalkind`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Goldberg2011, goldberg2011preemption. key=`Goldberg2011;goldberg2011preemption`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: HuddlestonPullum2002, huddleston2002. key=`HuddlestonPullum2002;huddleston2002`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Kutas2011, kutas2011thirty. key=`Kutas2011;kutas2011thirty`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Traugott1993, hopper1993. key=`Traugott1993;hopper1993`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: ambridge2019, ambridge2020radical. key=`ambridge2019;ambridge2020radical`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: bybee1994, bybee2015. key=`bybee1994;bybee2015`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: bybee2010, bybee2010usage. key=`bybee2010;bybee2010usage`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: chomsky1957, chomsky1957syntactic. key=`chomsky1957;chomsky1957syntactic`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: craver2007, craver2007explaining. key=`craver2007;craver2007explaining`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: croft2001, croft2001radical. key=`croft2001;croft2001radical`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: cuneogoldberg2023, cuneogoldberg2023Discourse. key=`cuneogoldberg2023;cuneogoldberg2023Discourse`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: goldberg2006, goldberg2006constructions. key=`goldberg2006;goldberg2006constructions`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: jackendoff2002, jackendoff2002foundations, jackendoff2002parallel. key=`jackendoff2002;jackendoff2002foundations;jackendoff2002parallel`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: kirby2015, kirby2015compression. key=`kirby2015;kirby2015compression`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: labov2006, labov2006atlas. key=`labov2006;labov2006atlas`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: lewis1969, lewis1969convention. key=`lewis1969;lewis1969convention`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: link1983, link1983plurals. key=`link1983;link1983plurals`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: machamer2000, machamer2000thinking. key=`machamer2000;machamer2000thinking`
  Suggestion: Manually inspect and merge if records are the same work.
- ... 5 more
