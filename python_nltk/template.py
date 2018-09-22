# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# template.py
#
# I realized that people who are brand new to NLP. They will most
# start just I like I did. This template will serve as way to help
# others navigate what to do when they want to clean their text
#
# -----------------------------------------------------------

# Imports
# ----------------------------------------------------
import functions as func

# First You need to Open a file that contains the data you
# will be working with. Here I am starting with Json File
# You can view sample_test.json to see what it contains
# 
# Open Json File
file = "./JSON/sample_test.json"
json_data = func.open_json(file)

# Now we need to store the information in a data structure. In
# Python we can use Dictionary which will store data using a
# key, value pair
# Created a dictionary whose value contains clean post_content data
post_dict = func.clean_dictionary(json_data)
