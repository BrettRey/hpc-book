# Full Bib Audit (2026-02-22)

## Summary
- Bib sources loaded: 1
- Total entries: 811
- Unique keys: 811
- Total issues: 69
- Errors: 0
- Warnings: 30
- Info: 39

## Bib Sources
- `/Users/brettreynolds/Documents/LLM-CLI-projects/.house-style/references.bib`

## Field Style Snapshot
- Journal fields: `journal`=362, `journaltitle`=5, both=0
- Time fields: `year`=806, `date`=1, both=4
- Place fields: `address`=349, `location`=9, both=0

## Issues By Code
- `case_collision_key`: 13
- `duplicate_doi_record`: 12
- `invalid_year_format`: 1
- `missing_required_field`: 4
- `mixed_address_location_style`: 1
- `mixed_journal_field_style`: 1
- `mixed_year_date_style`: 1
- `possible_duplicate_record`: 36

## Issue Details
### `case_collision_key` (13)
- [warning] Case-colliding keys share lowercase form `carlson1977`: Carlson1977, carlson1977.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `corbett1991`: Corbett1991, corbett1991.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `downing1996`: Downing1996, downing1996.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `haspelmath1997`: Haspelmath1997, haspelmath1997.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `haspelmath2010`: Haspelmath2010, haspelmath2010.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `huddleston2002`: Huddleston2002, huddleston2002.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `lakoff1987`: Lakoff1987, lakoff1987.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `lyons1999`: Lyons1999, lyons1999.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `millikan1984`: Millikan1984, millikan1984.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `quirk1985`: Quirk1985, quirk1985.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `rosch1973`: Rosch1973, rosch1973.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `rosch1975`: Rosch1975, rosch1975.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.
- [warning] Case-colliding keys share lowercase form `sperber1996`: Sperber1996, sperber1996.
  Suggestion: Choose one canonical key casing and update citations/references accordingly.

### `duplicate_doi_record` (12)
- [warning] DOI `10.1007/bf00385837` is shared by multiple keys: Boyd1991HPC, boyd1991, boyd1991realism. key=`Boyd1991HPC;boyd1991;boyd1991realism` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1017/cbo9781139166119` is shared by multiple keys: Corbett1991, corbett1991. key=`Corbett1991;corbett1991` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1038/s41583-024-00802-4` is shared by multiple keys: Fedorenko2024a, Fedorenko2024naturalkind. key=`Fedorenko2024a;Fedorenko2024naturalkind` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1515/cogl.2011.006` is shared by multiple keys: Goldberg2011, goldberg2011preemption. key=`Goldberg2011;goldberg2011preemption` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1353/lan.2010.0021` is shared by multiple keys: Haspelmath2010, haspelmath2010. key=`Haspelmath2010;haspelmath2010` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1017/9781009085748` is shared by multiple keys: Huddleston2021, HuddlestonPullumReynolds2022. key=`Huddleston2021;HuddlestonPullumReynolds2022` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1016/0010-0285(73)90017-0` is shared by multiple keys: Rosch1973, rosch1973. key=`Rosch1973;rosch1973` field=`doi`
  Suggestion: Merge duplicate records under one key and update citation usage.
- [warning] DOI `10.1037/0096-3445.104.3.192` is shared by multiple keys: Rosch1975, rosch1975. key=`Rosch1975;rosch1975` field=`doi`
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
- [info] Mixed use of `address` (349) and `location` (9).
  Suggestion: Choose one location field style and normalize.

### `mixed_journal_field_style` (1)
- [info] Mixed use of `journal` (362) and `journaltitle` (5).
  Suggestion: Choose one field style for articles and normalize across the bibliography.

### `mixed_year_date_style` (1)
- [info] Mixed use of `year` (806) and `date` (1).
  Suggestion: Normalize to house style (typically keep `year`, optionally also `date` when needed).

### `possible_duplicate_record` (36)
- [info] Same title+first-author+year signature appears under multiple keys: Boyd1991HPC, boyd1991, boyd1991realism. key=`Boyd1991HPC;boyd1991;boyd1991realism`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Carlson1977, carlson1977. key=`Carlson1977;carlson1977`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Corbett1991, corbett1991. key=`Corbett1991;corbett1991`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Fedorenko2024a, Fedorenko2024naturalkind. key=`Fedorenko2024a;Fedorenko2024naturalkind`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Goldberg2011, goldberg2011preemption. key=`Goldberg2011;goldberg2011preemption`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Haspelmath1997, haspelmath1997. key=`Haspelmath1997;haspelmath1997`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Haspelmath2010, haspelmath2010. key=`Haspelmath2010;haspelmath2010`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Huddleston2002, HuddlestonPullum2002, huddleston2002. key=`Huddleston2002;HuddlestonPullum2002;huddleston2002`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Kutas2011, kutas2011thirty. key=`Kutas2011;kutas2011thirty`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Lakoff1987, lakoff1987. key=`Lakoff1987;lakoff1987`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Lyons1999, lyons1999. key=`Lyons1999;lyons1999`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Millikan1984, millikan1984. key=`Millikan1984;millikan1984`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Quirk1985, quirk1985. key=`Quirk1985;quirk1985`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Rosch1973, rosch1973. key=`Rosch1973;rosch1973`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Rosch1975, rosch1975. key=`Rosch1975;rosch1975`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Sperber1996, sperber1996. key=`Sperber1996;sperber1996`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: Traugott1993, hopper1993. key=`Traugott1993;hopper1993`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: ambridge2019, ambridge2020radical. key=`ambridge2019;ambridge2020radical`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: bybee1994, bybee2015. key=`bybee1994;bybee2015`
  Suggestion: Manually inspect and merge if records are the same work.
- [info] Same title+first-author+year signature appears under multiple keys: bybee2010, bybee2010usage. key=`bybee2010;bybee2010usage`
  Suggestion: Manually inspect and merge if records are the same work.
- ... 16 more
