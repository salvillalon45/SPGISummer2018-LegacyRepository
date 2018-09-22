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


# Imports
# ----------------------------------------------------
import functions as func


# The Program
# ----------------------------------------------------

# Open Json File
file = "./JSON/working_data.json"
json_data = func.open_json(file)

# Create a list that contains the title of each post
posts_title = func.get_post_titles(json_data)

# Created a dictionary whose value contains clean post_content data
post_dict = func.clean_dictionary(json_data)

# The amount of frequent words to show
amount = 30

# Used to index the posts_title list
post_title_index = 0;

for id, post in post_dict.items():
    post = post.split()
    print("------------------------------------------------------- ")
    print("Post Number -- ", post_title_index + 1)
    print("Post Title  -- ", posts_title[post_title_index])
    print("Post ID     -- ", id)
    print(" ")
    print(amount, " Top Frequent Words")
    print(func.freq_words(post, amount))
    print(" ")
    print(" ")
    post_title_index += 1
