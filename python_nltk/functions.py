# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# functions.py
#
# I realized that I was copying and pasting many lines of code
# Making functions will make code cleaner and easier to read
#
# Inspiration from NLTK Book Chapter 4 http://www.nltk.org/book/ch04.html
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
from nltk import FreqDist
from nltk.stem.wordnet import WordNetLemmatizer
import math
from textblob import TextBlob as tb
import nltk
import json
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# Open a Json File
# ----------------------------------------------------
def open_json(file) -> str:
    """
    Open a Json File
    """
    json_data = json.load(open(file,encoding="latin-1"))
    return json_data


# Get the title of each post
# ----------------------------------------------------
def get_post_titles(json_data) -> list:
    """
    Get the title of each post
    """
    posts_title = list()
    for post in json_data:
        post_title = remove_chars(post["post_title"])
        posts_title.append(post_title)

    return posts_title


# Created a dictionary whose value contains clean post_content data
# key - post_id
# value - post_content
# value will contain the content of the post, with remove html tags
# and http links. It will also remove stopwords
# ----------------------------------------------------
def clean_dictionary(json_data) -> dict:
    """
     Created a dictionary whose value contains clean post_content data
    """
    post_dict = dict()
    for post in json_data:
        post_dict[post["ID"]] = post["ID"]
        post_dict[post["ID"]] = remove_html_http(post["post_content"])
        post_dict[post["ID"]] = remove_stopwords(post_dict[post["ID"]])
        post_dict[post["ID"]] = remove_chars(post_dict[post["ID"]])
        post_dict[post["ID"]] = lemmatize_remove_stopwords(post_dict[post["ID"]])
    return post_dict


# Turn text into an NLTK Text Object
# ----------------------------------------------------
def into_nltk_text(text_only) -> nltk:
    """
    Turn text into an NLTK Text Object
    """
    # Make text into tokens When I create tokens I will get
    # a list like this one ['If', 'you', 'add',...]
    tokens = nltk.word_tokenize(text_only)

    # Turn our tokens into an NLTK Text Object
    nltk_text = nltk.Text(tokens)

    return nltk_text


# Measures how frequently a term occurs in a document
# ----------------------------------------------------
def term_frequency(find_word, blob) -> int:
    """
    Measures how frequently a term occurs in a document
    """
    result = blob.words.count(find_word) / len(blob.words)
    return result


# returns the number of documents containing the word we are looking for
# ----------------------------------------------------
def n_containing(find_word, bloblist) -> int:
    """
    returns the number of documents containing the word we are looking for
    """
    result = 0
    for blob in bloblist:
        if find_word in blob.words:
            result = result + 1
    return result


# measures how common a word is among all documents in bloblist.
# The more common a word is, the lower its idf.
# Add 1 to the divisor to prevent division by zero.
# ----------------------------------------------------
def inverse_document_frequency(find_word, bloblist) -> float:
    """
    Measures how important a term is
    """
    result = math.log(len(bloblist) / (1 + n_containing(find_word, bloblist)))
    return result


# computes the TF-IDF score. It's the product of tf and idf.
# tfidf says how important that word is to that document with respect to the corpus
# IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
# Good Example Here - https://www.quora.com/How-does-TfidfVectorizer-work-in-laymans-terms
# ----------------------------------------------------
def term_frequency_idf(find_word, blob, bloblist):
    """
    computes the TF-IDF score. It's the product of tf and idf.
    """
    return term_frequency(find_word, blob) * inverse_document_frequency(find_word, bloblist)


# Remove http:// from the content of the blog post and
# normalizing whitespace and stripping HTML markup
# ----------------------------------------------------
def remove_html_http(raw_text) -> str:
    """
    Remove http:// from the content of the blog post and
    normalizing whitespace and stripping HTML markup
    """
    result = re.sub(r"http\S+", "", raw_text)
    result = re.sub(r'<.*?>', ' ', result)
    result = re.sub('\s+', ' ', result)
    soup = BeautifulSoup(result, "html.parser")
    text_only = soup.get_text()
    # print(" TEXT ONLY ")
    # print(text_only)
    # print(" ")
    return text_only


# Remove characters such as the
# ˜ Small Tilde
# â Latin Small Letter a with Circumflex
# ™ Trade Mark Sign
# € Euro Sign
# ----------------------------------------------------
def remove_chars(text) -> str:
    """
    Remove characters
    """
    # filtered_sentence = list()
    filtered_text = ""
    for w in text:
        w = w.lower()

        # ˜ Small Tilde
        if w == chr(0x02DC):
            w = w.replace(chr(0x02DC), "'")
            filtered_text = filtered_text + w

        # â Latin Small Letter a with Circumflex
        elif w == chr(0x00E2):
            w = w.replace(chr(0x00E2), "")
            filtered_text = filtered_text + w

        # ™ Trade Mark Sign
        elif w == chr(0x2122):
            w = w.replace(chr(0x2122), "'")
            filtered_text = filtered_text + w

        # € Euro Sign
        elif w == chr(0x20AC):
            w = w.replace(chr(0x20AC), "")
            filtered_text = filtered_text + w

        # Add the character to rest of the characters
        else:
            filtered_text = filtered_text + w

    # print(" REMOVE CHARACTERS ")
    # print(filtered_text)
    # print(" ")
    return filtered_text


# Remove stopwords from the text
# Also, we make sure the each word is lowercase. We do not want to
# to have the same word that is Uppercase and Lowercase as
# part of the Top 3 Words when we do TF-IDF
# ----------------------------------------------------
def remove_stopwords(text) -> str:
    """
    Remove stopwords from text
    """
    stop_words = set(stopwords.words('english'))
    # Removing Stopwords from nltk_text
    filtered_sentence = list()
    for w in text.split():
        w = w.lower()
        if w not in stop_words:
            filtered_sentence.append(w)

    noise_free_text = " ".join(filtered_sentence)
    # print(" REMOVE STOPWORDS ")
    # print(noise_free_text)
    # print(" ")
    return noise_free_text


# Lemmatize the text and Remove stopwords from the text
# Also, we make sure the each word is lowercase. We do not want to
# to have the same word that is Uppercase and Lowercase as
# part of the Top 3 Words when we do TF-IDF
# ----------------------------------------------------
def lemmatize_remove_stopwords(text) -> str:
    """
    Lemmatize the text and Remove stopwords from the text
    """
    lem = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    # Removing Stopwords from nltk_text
    filtered_sentence = list()
    for w in text.split():
        w = w.lower()
        if w not in stop_words:
            if w[-1] == "s":
                w = lem.lemmatize(w)
            else:
                w = lem.lemmatize(w, "v")
            filtered_sentence.append(w)

    noise_free_text = " ".join(filtered_sentence)
    # print(" REMOVE STOPWORDS AND LEMMATIZE ")
    # print(noise_free_text)
    # print(" ")
    return noise_free_text



# Find the most frequent words based on an amount the user gives
# ----------------------------------------------------
def freq_words(nltk_text, n) -> list:
    """
    Find the most frequent words based on an amount the user gives
    """
    freqdist = FreqDist(nltk_text)
    return freqdist.most_common(n)
