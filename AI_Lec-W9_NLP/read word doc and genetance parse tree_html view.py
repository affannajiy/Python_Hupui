"""
Dependencies Required:
pip install nltk python-docx spacy
python -m nltk.downloader punkt
python -m spacy download en_core_web_sm
"""

import nltk
import spacy
from nltk import CFG
from nltk.tree import Tree
from nltk.tokenize import sent_tokenize
from docx import Document
from spacy import displacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Download tokenizer
nltk.download('punkt')

# === Define a simple grammar with punctuation support ===
grammar = CFG.fromstring("""
  S -> NP VP | NP VP PUNCT
  NP -> Det N | Det Adj N | 'John' | 'Mary' | 'I'
  VP -> V NP | V
  Det -> 'a' | 'the' | 'my'
  N -> 'cat' | 'dog' | 'telescope' | 'man' | 'apple'
  V -> 'saw' | 'loved' | 'ate'
  Adj -> 'big' | 'small'
  PUNCT -> '.' | ',' | '?' | '!'
""")

cfg_parser = nltk.ChartParser(grammar)

# === Function to read sentences from Word document ===
def extract_sentences_from_docx(filepath):
    doc = Document(filepath)
    full_text = " ".join(para.text for para in doc.paragraphs if para.text.strip())
    return sent_tokenize(full_text)

# === Parse with NLTK CFG ===
def parse_with_cfg(sentence):
    tokens = nltk.word_tokenize(sentence)
    
    try:
        for tree in cfg_parser.parse(tokens):
            print(f"\nCFG Parse Tree for: \"{sentence}\"")
            print(tree)
            tree.pretty_print()
            break  # Only show first valid parse
    except ValueError as e:
        print(f"CFG parsing failed for: {sentence} | Reason: {e}")
    except Exception as e:
        print(f"Parsing error: {e}")

# === Parse with spaCy dependency parser ===
def parse_with_spacy(sentence):
    doc = nlp(sentence)
    print(f"\nDependency Parse for: \"{sentence}\"")
    for token in doc:
        print(f"{token.text:<10} -> {token.dep_:<10} (Head: {token.head.text})")

    # Optional: render and save HTML
    html = displacy.render(doc, style="dep")
    filename = "dependency_" + "_".join(sentence.split()[:3]) + ".html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

# === Main ===
def process_docx(filepath):
    sentences = extract_sentences_from_docx(filepath)
    print(f"Total sentences found: {len(sentences)}")
    
    for i, sent in enumerate(sentences):
        print(f"\n--- Sentence {i+1} ---")
        parse_with_cfg(sent)
        parse_with_spacy(sent)

# === Run ===
if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    print("Select a Word document (.docx) to process...")
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    
    if file_path:
        process_docx(file_path)
    else:
        print("No file selected.")
