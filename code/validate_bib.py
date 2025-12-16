import bibtexparser

try:
    with open('references.bib', 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    print("Successfully parsed references.bib")
except Exception as e:
    print(f"Error parsing references.bib: {e}")
