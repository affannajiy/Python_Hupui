import nltk
from nltk import CFG

#Download tokenizer once
nltk.download('punkt')

#User defined grammar
ambiguous_grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP | 'I'
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the'
    N -> 'man' | 'telescope'
    V -> 'saw'
    P -> 'with'
""")

# Create parser
parser = nltk.ChartParser(ambiguous_grammar)

# Ambiguous sentence
sentence = "I saw the man with the telescope"
tokens = nltk.word_tokenize(sentence)

print("Ambiguous Parse Trees:")
for tree in parser.parse(tokens):
    print(tree)
    tree.pretty_print()
