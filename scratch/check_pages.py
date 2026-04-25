import fitz
doc = fitz.open('PAUL BOUBERT _PORTFOLIO 2025.pdf')
for i in range(min(15, len(doc))):
    text = doc[i].get_text().strip().replace('\n', ' ')
    print(f"Index {i}: {text[:100]}")
