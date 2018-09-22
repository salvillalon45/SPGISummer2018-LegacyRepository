# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# entity_extraction.py
# Here I am practicing Entity Extraction in NLTK
#
# The Definition
# Entities are defined as the most important chunks of a sentence
#
# https://sambitach.wordpress.com/2016/01/26/3-ways-to-perform-named-entity-recognition-in-python/
# http://www.nltk.org/book/ch07.html Section 5
# https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
# https://towardsdatascience.com/topic-modelling-in-python-with-nltk-and-gensim-4ef03213cd21
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
import nltk
import nltk.corpus
from gensim import corpora
import gensim
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
import random


# The Program
# ----------------------------------------------------

# Using NLTK for performing Named Entity Recognition
# ----------------------------------------------
# If we set the parameter binary=True [1], then named entities are just tagged as NE
sent = nltk.corpus.treebank.tagged_sents()[22]
# print(nltk.ne_chunk(sent, binary=True))

# otherwise, the classifier adds category labels such as PERSON, ORGANIZATION, and GPE.
sent = nltk.corpus.treebank.tagged_sents()[22]
# print(nltk.ne_chunk(sent))


# Topic Modeling (Based on analyticsvidhya.com)
# ----------------------------------------------
doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father."
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."

doc_complete = [doc1, doc2, doc3]
doc_clean = [doc.split() for doc in doc_complete]

# Creating the term dictionary of our corpus,
# where every unique term is assigned an index
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix
# using dictionary prepared above
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim libary
# Running and Training LDA model on the document term matrix
ldamodel = gensim.models.ldamodel.LdaModel(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

# The Results
topics = ldamodel.print_topics()
for topic in topics:
    print(topic)

# N-Grams as Features
# ----------------------------------------------
# A combination of N words together are called N-Grams.
def generate_ngrams(text, n):
    words = text.split()
    output = list()
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    return output

print(generate_ngrams("this is a sample text", 2))
