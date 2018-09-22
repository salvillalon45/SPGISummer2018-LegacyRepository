# -----------------------------------------------------------
# Salvador Villalon SPDJI Summer 2018 Intern
# NLP Learning
# readme
#
# A readme file to get started with Python and NLP
#
# -----------------------------------------------------------

Hello,

My name is Salvador Villalon and I am Software Developer Intern
at S&P Dow Jones Indices for Summer 2018.

My manager Sharath Srinivas asked to explore what we can do with
Python and NLTK. Here you will find some of the concepts I worked
with.

Make sure you read the notes/notes.txt. There you will find some
of the characters I had to remove to be able to parse the text

First, I recommend that you use virtualenv
- Learn more here:
  - https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv
  - https://virtualenv.pypa.io/en/stable/

Second, install the packages that I used
 - Once you activated your virtual environment Install the packages
   that I used from requirements.txt


JSON Directory
# -----------------------------------------------------------
- original_data.json
  - Contains the original post information. This is the information
    as it would like when you first export it out of your MySQL
    workbench

- sample_test.json
  - Since there were a lot of post, I just picked seven to start
    experimenting with

- working_data.json
  - Contains the all of the posts, but with the characters that
    did not allowed us to run the file. Check the notes.txt to see
    which characters I removed.


Notes Directory
# -----------------------------------------------------------
- notes.txt
  - This .txt contains notes that I took on important things I
    noticed. Make sure to look at it


Pictures Directory
# -----------------------------------------------------------
- unicode_error.PNG
    - This picture displays a constant error I faced when I was
      working on this project.


SQL Directory
# -----------------------------------------------------------
- join_query.sql
  - This query joins two tables: wp_users and wp_posts so
    that we can get the five values listed on the select statement

- post_data.sql
  - This file contains the entire table for wp_posts. You can use
    this in case you accidentaly drop a table in the original
    table. (Just like I did when I first started, sorry Sharath,
    but I was able to figure it out!)


Tutorial Directory
# -----------------------------------------------------------
- This Directory contains what I did to practice the concepts
  that I learned from these sources
  https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
  http://www.nltk.org/book/


Virtual Directory
# -----------------------------------------------------------
- Everything needed to run your virtualenv environment


Python Modules
# -----------------------------------------------------------
- functions.py
  - A module that contains functions for lines of code that I used
    very often throughout my experimentations

- summarizer.py
  - A module that where I practice how to summarize a text

- tf_idf.py
  - A module that helps determine the TF-IDF score. A rate on
    how important the word is to the document.
  - Something strange occurred on line 32 - 33 of the Module
    When I tried using blob.words on a single word of 'talked'
    the ending quote disappears so that it looks like this: 'talked

- ranking.py
  - A module to determine what are the most frequent words used
    in a blog post
