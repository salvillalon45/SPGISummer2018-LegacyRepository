# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# syntactic_parsing.py
# Here I am practicing the idea behind Syntactic Parsing
#
# The Definition
# Syntactical parsing involves the analysis of words in the sentence
# for grammar and their arrangement in a manner that shows the
# relationships among the words.
#
# https://likegeeks.com/nlp-tutorial-using-python-nltk/
# http://www.nltk.org/book/ch08.html Section 5
# https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
import nltk
from nltk import word_tokenize, pos_tag


# The Program
# ----------------------------------------------------

# Dependencies and Dependency Graphs
# ----------------------------------------------
groucho_dep_grammar = nltk.DependencyGrammar.fromstring(
    """
    'shot' -> 'I' | 'elephant' | 'in'
    'elephant' -> 'an' | 'in'
    'in' -> 'pajamas'
    'pajamas' -> 'my'
    """)

print(groucho_dep_grammar)

groucho_dep_grammar = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = "I shot an elephant in my pajamas".split()
trees = groucho_dep_grammar.parse(sent)
for tree in trees:
    print(tree)


# Part of Speech Tagging
# ----------------------------------------------
text = "I am learning Natural Language Processing on Analytics Vidhya"
tokens = word_tokenize(text)
print(pos_tag(tokens))
