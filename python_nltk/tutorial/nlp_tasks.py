# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# nlp_tasks.py
# Here I am practicing se cases and problems in the field of natural language processing using NLTK
#
# The Definition
# This section talks about different use cases and problems in the field of natural language processing.
#
# https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
# http://www.nltk.org/book/ch06.html
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
import nltk
from nltk.corpus import names
import random
import fuzzy
import math
from collections import Counter


# The Program
# ----------------------------------------------------

# Text Classification (Example from NLKT Book Ch. 6)
# ----------------------------------------------
def gender_features(word):
    return { "last_letter": word[-1] }

labeled_names = ([(name, "male") for name in names.words("male.txt")] + [(name, "female") for name in names.words("female.txt")])
random.shuffle(labeled_names)

feature_sets = [(gender_features(n), gender) for (n, gender) in labeled_names]
# feature_sets[500:] --- Give everything starting from 500
# feature_sets[:500] --- Give everything up to and including 500
train_set, test_set = feature_sets[500:], feature_sets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)


print(classifier.classify(gender_features("Neo")))
print(classifier.classify(gender_features("Trinity")))


# Text Matching / Similarity (Example from www.analyticsvidhya.com)
# ----------------------------------------------

# Levenshtein Distance
# ----------------------------------------------
def levenshtein(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1], distances[index1+1], newDistances[-1])))
        distances = newDistances
    return distances[-1]
print(levenshtein("analyze", "analyse"))


# Phonetic Matching
# ----------------------------------------------
soundex = fuzzy.Soundex(4)
print(soundex('ankit'))
print(soundex('aunkit'))


# Cosine Similarity
# ----------------------------------------------
def get_cosine(vec1, vec2):
    common = set(vec1.keys() & set(vec2.keys()))
    numerator = sum([vec1[x] * vec2[x] for x in common])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = text.split()
    return Counter(words)

text1 = 'This is an article on analytics vidhya'
text2 = 'article on analytics vidhya is about natural language processing'
text1 = "hola"
text2 = "hole"
vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)
print(cosine)
