# Create a solution file that combines the function searching for the book title, author, translator and illustrator
# with the search for specified keywords
# import regex and sys library
import re
import sys

# import the variables DIV_COMM and MAG_CART from pg_sample_texts.py
from pg_sample_texts import DIV_COMM, MAG_CART

# assign DIV_COMM and MAG_CART to a variable list - documents
documents = [DIV_COMM, MAG_CART]

# create an empty dictionary to store searches
searches = {}

# generate a regex pattern for each keyword specified using index 1 which is after the file name specified
for kw in sys.argv[1:]:
    searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)

# generate regex patterns for the title, author, translator and illustrator
title_search = re.compile(r'(title:\s*)(?P<title>[a-zA-Z, \n]* \s)', re.IGNORECASE)
author_search = re.compile(r'(author:*)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:*)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:*)(?P<illustrator>.*)', re.IGNORECASE)

# iterate through the documents getting the title, author, translator and illustrator and the number of times
# the specified keyword appears in the document
for i, doc in enumerate(documents):
    title = re.search(title_search, doc).group('title')
    author = re.search(author_search, doc)
    translator = re.search(translator_search, doc)
    illustrator = re.search(illustrator_search, doc)

    # group the author, translator, and illustrator
    if author:
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')

    # print out the results
    print "***" * 25
    print "Here are the results for the document {}".format(i+1)
    print "The title of the text is {}".format(title)
    print "The author is {}".format(author)
    print "The translator is {}".format(translator)
    print "The illustrator is {}".format(illustrator)
    print ""

    # search for the specified keyword(s) as well in the document and print
    print "Here's the counts for the keywords you searched for:"
    for search in searches:
        kw_count = len(re.findall(searches[search], doc))
        print "\"{0}\": {1}".format(search, kw_count)
    print "***" * 25
    print "\n"

