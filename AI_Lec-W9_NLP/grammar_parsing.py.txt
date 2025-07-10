import nltk
from nltk import CFG

# Download required resources (only run once)
nltk.download('punkt')

# 1. Define a simple grammar (Context-Free Grammar)
grammar = CFG.fromstring("""
  S -> NP VP
  NP -> Det N | Det Adj N | 'John' | 'Mary'
  VP -> V NP | V
  Det -> 'a' | 'the'
  N -> 'cat' | 'dog' | 'telescope' | 'man'
  V -> 'saw' | 'loved' | 'ate'
  Adj -> 'big' | 'small'
""")

# 2. Create a parser
parser = nltk.ChartParser(grammar)

# 3. Input sentence to parse
sentence = "the big dog saw a cat"
tokens = nltk.word_tokenize(sentence)

# 4. Generate and print parse trees
print("Parse Trees:")
for tree in parser.parse(tokens):
    print(tree)
    tree.pretty_print()
