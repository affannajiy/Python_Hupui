#Option A: pretty_print() in NLTK (built-in)
#tree.pretty_print()

#Option B: Save Parse Tree as an Image Using pydot + graphviz
import nltk
import pydot
from nltk.tree import Tree
from IPython.display import Image

# Example tree (you can replace this with any parsed tree)
tree = Tree.fromstring("(S (NP I) (VP (V saw) (NP (Det the) (N man))))")

# Draw and save
tree.draw()  # Opens a GUI window

# Or export as image if using Jupyter:
def display_tree(tree):
    from nltk.draw.util import CanvasFrame
    from nltk.draw import TreeWidget

    cf = CanvasFrame()
    tc = TreeWidget(cf.canvas(), tree)
    cf.add_widget(tc, 10, 10)
    cf.print_to_file("nltk_tree.ps")
    cf.destroy()

# display_tree(tree)  # This saves a .ps file you can convert to PNG


#Dependency Graph Visualization with spaCy + displacy

#Option A: Show Inline in Jupyter
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("The quick brown fox jumps over the lazy dog")

# Display in notebook
displacy.render(doc, style='dep', jupyter=True)


#Option B: Export to HTML
# Render as HTML string
html = displacy.render(doc, style="dep")

# Save to file
with open("dependency_parse.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved dependency graph to dependency_parse.html")

