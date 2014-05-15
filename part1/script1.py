import re

# import the DIV_COMM and MAG_CART strings from pg_sample_texts.py
from pg_sample_texts import DIV_COMM, MAG_CART

# assign DIV_COMM, MAG_CART to a variable list called documents
documents = [DIV_COMM, MAG_CART]

# create regex patterns metadata search for the title, author, translator and illustrator using re.compile() method
#title_search = re.compile(r'(title:\s*)(?P<title>.*)', re.IGNORECASE)
# create regex pattern that caters for multiple lines
title_search = re.compile(r'(title:\s*)(?P<title>[a-zA-Z, \n]* \s)',  re.IGNORECASE )
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

# iterate over the documents (using enumerate) by searching for patterns and extracting the metadata printing the output 
for i, doc in enumerate(documents):
	title = re.search(title_search, doc).group('title')
	author = re.search(author_search, doc)
	translator = re.search(translator_search, doc)
	illustrator = re.search(illustrator_search, doc)
	
	# group the author, translator, and illustrator into relevant groups
	if author:
		author = author.group('author')
	if translator:
		translator = translator.group('translator')
	if illustrator:
		illustrator = illustrator.group('illustrator')
	
	# print out the results
	print "***" * 25
	print ""
	print "Here is the information for doc {0}".format(i)
	print "Title: {}".format(title)
	print "Author: {}".format(author)
	print "Translator: {}".format(translator)
	print "Illustrator: {}".format(illustrator)
	print "\n"
	


