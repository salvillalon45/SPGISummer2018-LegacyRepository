# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# statistical_features.py
# Here I am practicing Statistical Features in NLTK
#
# The Definition
# Text data can also be quantified directly into numbers using several techniques
#
# http://www.nltk.org/book/ch01.html Section 1.4
# https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
import nltk
from gensim.models import Word2Vec


# The Program
# ----------------------------------------------------

# Term Frequency – Inverse Document Frequency (TF – IDF)
# ----------------------------------------------
text = "Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions. However, Flask supports extensions that can add application features as if they were implemented in Flask itself. Extensions exist for object-relational mappers, form validation, upload handling, various open authentication technologies and several common framework related tools. Extensions are updated far more regularly than the core Flask program. Flask is commonly used with MongoDB which allows it more control over databases and history."
tokens = text.split()
# print(len(tokens))

# Calculate percentage of distinct words in a text
def lexical_diversity(tokens):
    per = len(set(tokens)) / len(tokens)
    print("Percentage of Distinct Words in the text " , per)
    return per

# print(lexical_diversity(tokens))
# We will get a result of 0.819047619047619
# The example shows us that the number of distinct words is 80%
# Count amount of time a word appears in the text
word_to_look_for = "Flask"
word_count = tokens.count(word_to_look_for)
total_words = len(tokens)

def percentage(word_to_look_for, word_count, total_words):
    amount = 100 * word_count / total_words
    print("The word " , word_to_look_for, " appears " , amount , " in the text")
    return amount
print(percentage(word_to_look_for, word_count, total_words))


# Term Frequency – Inverse Document Frequency (TF – IDF) Formula
from sklearn.feature_extraction.text import TfidfVectorizer
obj = TfidfVectorizer()
corpus = ['This is sample document.', 'another random document.', 'third sample document text']

# fit_transform returns term-document matrix
X = obj.fit_transform(tokens)
print(X)


# Word Embedding (text vectors)
# ----------------------------------------------
sentences = [['data', 'science'], ['vidhya', 'science', 'data', 'analytics'],['machine', 'learning'], ['deep', 'learning']]

# Train the model on your corpus
model = Word2Vec(sentences, min_count = 1)

print(model.similarity("data", "science"))
print(model["learning"])
