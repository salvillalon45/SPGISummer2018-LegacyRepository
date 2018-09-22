# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# text_processing.py
# Here I am practicing the idea behind Text Processing
#
# The Definition
# Text is the most unstructured form of all the available data,
# various types of noise are present in it and the data is not
# readily analyzable without any pre-processing.
# The entire process of cleaning and standardization of text,
# making it noise-free and ready for analysis is known as text preprocessing.
#
# https://likegeeks.com/nlp-tutorial-using-python-nltk/
# https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
import chardet
import nltk
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


# The Program
# ----------------------------------------------------

# It appears that urlopen() needs a website with https, not http
# It gave me a timeout error when I tried websites such as http://flask.pocoo.org/
response = urllib.request.urlopen('https://python.org/')
html = response.read()

# check what the character encoding might be
with urllib.request.urlopen('https://python.org/') as rawdata:
    result = chardet.detect(rawdata.read(10000))
# print(result)

# Tokenize Text Using Pure Python
# ----------------------------------------------
# This will get us the text without html tags
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)

# This will put all the words in the text
# in a list called tokens
tokens = list()
for t in text.split():
    tokens.append(t)


# Remove Stop Words Using NLTK
# It is better to remove the stop words first so That
# when we check the frequency distribution it does not
# include the stopwordsd
# ----------------------------------------------
clean_tokens = tokens[:]
stop_words = stopwords.words("english")
for token in tokens:
    if token in stop_words:
        clean_tokens.remove(token)

# Count word frequency
# ----------------------------------------------
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + " : " + str(val))

This graph shows us how many times a word appears
freq.plot(20, cumulative=False)




# Tokenize Text Using NLTK
# ----------------------------------------------
# Tokenize paragraph into sentences
text = "Hola Adam, como estas. Espero que todo este bien. Hoy es un gran dia. Te veo al rato, bro"
print(sent_tokenize(text))

# Tokenize paragraph into word
text = "Hola Senor Adam, como estas. Espero que todo este bien. Hoy es un gran dia. Te veo al rato, bro"
print(word_tokenize(text))


# Get Synonyms from WordNet
# ----------------------------------------------
syn = wordnet.synsets("Pokemon")

synonms = list()
for syn in wordnet.synsets("Computer"):
    for lemma in syn.lemmas():
        synonms.append(lemma.name())
print(synonms)

# Get Antonyms from WordNet
# ----------------------------------------------
antonyms = list()

for syn in wordnet.synsets("small"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
print(antonyms)

# NLTK Word Stemming
# ----------------------------------------------
stemmer = PorterStemmer()
print(stemmer.stem("playing"))


# Lemmatizing Words Using WordNet
# ----------------------------------------------
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("playing"))
# If you try to print you will noticed that it will
# be the same word. This is because the default part of speech is
# nouns. We have to change it to verbs
print(lemmatizer.lemmatize("playing", pos="v"))
