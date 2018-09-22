# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# ranking.py
#
# Here I am trying to see which words are the most used
# in the blog posts
#
#
# https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
# http://www.nltk.org/book/ch01.html
#
# The Most Common Relevant Words I found were
# index     445
# price     319
# 500       219
# commodity 287
# -----------------------------------------------------------

import nltk
import pprint
import json
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk import FreqDist



# JSON Parser and Putting Raw Text Into working_text.txt
# ----------------------------------------------------
json_data = json.load(open("./JSON/working_data.json"))
pp = pprint.PrettyPrinter(indent=4)

post_dict = dict()

for post in json_data:
    post_dict[post["ID"]] = post["ID"]
    post_dict[post["ID"]] = post["post_content"]


# Writing info from post_content column to a file
write_to_working_text = open("working_text.txt", "w")

for key,value in post_dict.items():
    write_to_working_text.write(value)
    write_to_working_text.write("\n")

write_to_working_text.close()

# Open working_text.txt for reading
nltk_file = open("working_text.txt", "rU")
nltk_raw_text = nltk_file.read()

# Create NLTK Text Object
# -----------------------------------------------
# Remove http:// from the content of the blog post
result = re.sub(r"http\S+", "", nltk_raw_text)

# With BeautifulSoup I am able to get the text
# without the html tags that appeared in the text
soup = BeautifulSoup(result, "html.parser")
text_only = soup.get_text()

# Make text into tokens When I create tokens I will get
# a list like this one ['If', 'you', 'add',...]
tokens = nltk.word_tokenize(text_only)

# Turn our tokens into an NLTK Text Object
nltk_text = nltk.Text(tokens)


# Clean the Text
# -----------------------------------------------
# Create Set of Stopwords to remove
stop_words = set(stopwords.words('english'))
# manual_stop_words = ["caption", "id=", "''", "attachment_953", "align=", "alignnone", "width=", "393"]
# Removing Stopwords from nltk_text
filtered_sentence = list()
for w in nltk_text:
    # if w not in manual_stop_words:
    #     filtered_sentence.append(w)
    if w not in stop_words:
        filtered_sentence.append(w)

# Write to output.txt
write_to_output_text = open("output.txt","w")

for i in filtered_sentence:
    write_to_output_text.write(i)
    write_to_output_text.write(" ")

write_to_output_text.close()

open_file = open("output.txt", "rU")
raw_text = open_file.read()
tokens = nltk.word_tokenize(raw_text)
nltk_text = nltk.Text(tokens)


# Collocations
# -----------------------------------------------
# A collocation is a sequence of words that occur together unusually often.
print(nltk_text.collocations())
