import spacy

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog"

# Parse sentence
doc = nlp(sentence)

# Display dependencies
print("Dependency Parsing:")
for token in doc:
    print(f"{token.text:<10} -> {token.dep_:<10} (Head: {token.head.text})")

# Optional: Visualize (if running in Jupyter Notebook)
# from spacy import displacy
# displacy.render(doc, style='dep', jupyter=True)