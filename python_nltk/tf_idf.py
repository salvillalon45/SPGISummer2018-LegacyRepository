# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# tf_idf.py
#
# Here I am trying to see which words are the most used
# in the blog posts
#
# https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
# http://www.nltk.org/book/ch01.html
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
import functions as func
from textblob import TextBlob as tb


# The Program
# ----------------------------------------------------

# Open Json File
file = "./JSON/sample_test.json"
json_data = func.open_json(file)

# Created a dictionary whose value contains clean post_content data
post_dict = func.clean_dictionary(json_data)

# Find the TF-IDF of the top three words in the document
bloblist = [tb(post_dict[2]), tb(post_dict[8]), tb(post_dict[43]), tb(post_dict[47]), tb(post_dict[48]), tb(post_dict[155]), tb(post_dict[1609])]

for i, blob in enumerate(bloblist):
    print("Top Words in document {}".format(i+1))
    # This will create a dictionary of each word in the document
    # Key - word
    # Value - TF-IDF score (Rate how important the word is to the document)

    # Error is here
    # print(blob.words)
    scores = {word: func.term_frequency_idf(word, blob, bloblist) for word in blob.words}

    # This will create a list of tuples starting with the words with highest TF-IDF score
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
