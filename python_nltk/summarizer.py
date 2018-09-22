# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# summarizer.py
#
# Here I am making a summarizer - an algorithm to reduce bodies of text
# but keeping its original meaning, or giving a great insight into
# the original text
#
# https://rare-technologies.com/text-summarization-with-gensim/
# -----------------------------------------------------------


# Imports
# ----------------------------------------------------
import functions as func
from gensim.summarization import keywords
from gensim.summarization import summarize


# The Program
# ----------------------------------------------------

# Open Json File
file = "./JSON/working_data.json"
json_data = func.open_json(file)

# This will contain the title of each post
posts_title = func.get_post_titles(json_data)

# This will contain the id of each post
posts_id = list()

# A list that contains each post
posts = list()

# Created a dictionary whose value contains post_content data
# We will only remove html tags, http links, and special characters
# from post_content since the summarizer() functions also takes care
# of stopwords and stemming
post_dict = dict()


for post in json_data:
    # posts_title.append(post["post_title"])
    post_dict[post["ID"]] = post["ID"]
    post_dict[post["ID"]] = func.remove_html_http(post["post_content"])
    post_dict[post["ID"]] = func.remove_chars(post_dict[post["ID"]])
    posts_id.append(post["ID"])
    posts.append(post_dict[post["ID"]])


post_id_index = 0
post_title_index = 0;

for post in posts:
    print("------------------------------------------------------- ")
    print("Post Number -- ", post_title_index + 1)
    print("Post Title  -- ", posts_title[post_title_index])
    print("Post ID     -- ", posts_id[post_id_index])
    print(" ")

    print("Summary -- Word Count")
    if (len(post.split()) <= 460):
        print("Not valid sentence since it does not have enough words")
    else:
        print(summarize(post, word_count=50))
        print(" ")

    print("Summary -- Ratio")
    if (len(post.split()) <= 460):
        print("Not valid sentence since it does not have enough words")
    else:
        print(summarize(post, ratio=0.5))
        print(" ")

    print("Keywords")
    if (len(post.split()) <= 460):
        print("Not valid sentence since it does not have enough words")
    else:
        print(keywords(post))

    print("------------------------------------------------------- ")
    print(" ")
    post_title_index += 1
    post_id_index += 1
