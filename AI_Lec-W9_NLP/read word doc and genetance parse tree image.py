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
import os
import uuid
from PIL import Image
import cairosvg

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Download tokenizer
nltk.download('punkt')

# Define CFG grammar with punctuation
grammar = CFG.fromstring("""
  S -> NP VP | NP VP PUNCT
  NP -> Det N | Det Adj N | 'John' | 'Mary' | 'I'
  VP -> V NP | V
  Det -> 'a' | 'the' | 'my'
  N -> 'cat' | 'dog' | 'telescope' | 'man' | 'apple'
  V -> 'saw' | 'loved' | 'ate'
  Adj -> 'big' | 'small'
  PUNCT -> '.' | '?' | '!' | ','
""")

cfg_parser = nltk.ChartParser(grammar)

# Create output directories
os.makedirs("output/cfg_trees", exist_ok=True)
os.makedirs("output/dep_trees", exist_ok=True)

# Extract sentences from DOCX
def extract_sentences_from_docx(filepath):
    doc = Document(filepath)
    full_text = " ".join(p.text for p in doc.paragraphs if p.text.strip())
    return sent_tokenize(full_text)

# Save CFG Tree to image
def save_cfg_tree_image(tree, filename):
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget

    cf = CanvasFrame()
    widget = TreeWidget(cf.canvas(), tree)
    cf.add_widget(widget, 10, 10)
    ps_path = os.path.join("output/cfg_trees", filename + ".ps")
    cf.print_to_file(ps_path)
    cf.destroy()

# Save spaCy dependency tree to PNG via SVG
def save_spacy_dependency_image(doc, filename):
    svg = displacy.render(doc, style="dep", jupyter=False)
    svg_path = os.path.join("output/dep_trees", filename + ".svg")
    png_path = os.path.join("output/dep_trees", filename + ".png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg)

    cairosvg.svg2png(url=svg_path, write_to=png_path)

# Process a single sentence
def process_sentence(sentence, index):
    print(f"\nProcessing Sentence {index+1}: {sentence}")
    tokens = nltk.word_tokenize(sentence)

    # CFG Parsing
    try:
        for tree in cfg_parser.parse(tokens):
            print(tree)
            tree.pretty_print()
            save_cfg_tree_image(tree, f"cfg_tree_{index+1}")
            break
    except Exception as e:
        print("CFG Parsing failed:", e)

    # Dependency Parsing
    doc = nlp(sentence)
    save_spacy_dependency_image(doc, f"dep_tree_{index+1}")

# Main processor
def process_docx(filepath):
    sentences = extract_sentences_from_docx(filepath)
    print(f"\nFound {len(sentences)} sentences.")

    for idx, sent in enumerate(sentences):
        process_sentence(sent, idx)

# Entry point
if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    print("Select a Word document (.docx)...")
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])

    if file_path:
        process_docx(file_path)
        print("\n✅ All sentence trees saved to 'output/' folders.")
    else:
        print("❌ No file selected.")