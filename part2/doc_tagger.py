# program that parses through text documents in folder and prints title, author, illustrator, etc and keyword details

# import the os, re and sys modules
import os
import sys
import re

# assign the directory name entered in the terminal to a variable directory
directory = sys.argv[1]

# create an empty dictionary for the keywords
keyword_searches = {}

# generate regex pattern for keywords specified from the terminal from 2 index after the directory
for keywords in sys.argv[2:]:
    keyword_searches[keywords] = re.compile(r'\b '+ keywords + r'\b', re.IGNORECASE)

# generate regex patterns for title, author, illustrator and translator
title_search = re.compile(r'(title:\s*)(?P<title>[a-zA-Z, \n].* \s)', re.IGNORECASE|re.VERBOSE)
author_search = re.compile(r'(author:*)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:*)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:*)(?P<illustrator>.*)', re.IGNORECASE)


# iterate through all the files in the directory
for doc_no, file_name in enumerate(os.listdir(directory)):
    file_path = os.path.join(directory, file_name)  # assign the full path of the file name by adding the directory path

    # open each file and read from it assigning the text to a variable file_text
    with open(file_path, 'r') as read_file:
        file_text = read_file.read()

    # group the title, author, translator and illustrator and print details

    title = re.search(title_search, file_text).group('title')
    author = re.search(author_search, file_text)
    translator = re.search(translator_search, file_text)
    illustrator = re.search(illustrator_search, file_text)

    if author:
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')

    # print out the results
    print "***" * 25
    print ""
    print "Here are the info for file {}".format(file_name)
    print "The title of the text is {}".format(title)
    print "The author is {}".format(author)
    print "The translator is {}".format(translator)
    print "The illustrator is {}".format(illustrator)
    print ""

    # count how many times the keywords searched for appear in the searched texts and print
    print "Here is the counts for the keywords searched:"

    for keyword in keyword_searches:
        keyword_count = len(re.findall(keyword, file_text))
        print "\"{0}\": {1}".format(keyword, keyword_count)

    print ""
    




