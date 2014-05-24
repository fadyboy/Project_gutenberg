import os
import sys
import re


def keywordPatterns(keywords):
    '''
        This function generates a regex pattern for each user supplied keyword at runtime
    '''
    keyword_patterns = {}   # create an empty dictionary for keyword patterns
    for keyword in keywords:
        keyword_patterns[keyword] = re.compile(r'\b' + keyword + r'\b', re.IGNORECASE)

    return keyword_patterns


def keywordCount(keywords, text):
    '''
        This function counts the number of times a keyword appears in a document
        It finds all words that match the keyword_patterns in the text
    '''
    # assign the value of keywordPatterns function to the variable keyword_searches
    keyword_searches = keywordPatterns(keywords)
    for keyword in keyword_searches:
        keyword_count = len(re.findall(keyword_searches[keyword], text))
        print "Here is the count(s) for the keywords searched \n"
        print "\"{0}\": {1}".format(keyword, keyword_count)


def documentMetadata():
    '''
        This function generates regex patterns for the title, author, translator, and illustrator in documents
    '''
    # create an empty list for document metadata patterns
    doc_metadata = []

    # generate the regex patterns
    title_search = re.compile(r'(title:\s*)(?P<title>[a-zA-Z, \n].* \s)', re.IGNORECASE|re.VERBOSE)
    author_search = re.compile(r'(author:*)(?P<author>.*)', re.IGNORECASE)
    translator_search = re.compile(r'(translator:*)(?P<translator>.*)', re.IGNORECASE)
    illustrator_search = re.compile(r'(illustrator:*)(?P<illustrator>.*)', re.IGNORECASE)

    # add search patterns to doc_metadata dictionary
    doc_metadata.append(title_search)
    doc_metadata.append(author_search)
    doc_metadata.append(translator_search)
    doc_metadata.append(illustrator_search)

    return doc_metadata


def getFiles(directory):
    '''
        This function iterates over all the files in the folder specified at runtime and prints the outputs
    '''

    # use document metadata search patterns to search for document details
    search_patterns = documentMetadata()

    for file_name in os.listdir(directory):
        if file_name.endswith('.txt'):
            file_path = os.path.join(directory, file_name)

            # open each file and read from it
            with open(file_path, 'r') as read_file:
                file_text = read_file.read()

            title = re.search(search_patterns[0],file_text).group('title')
            author = re.search(search_patterns[1], file_text)
            translator = re.search(search_patterns[2], file_text)
            illustrator = re.search(search_patterns[3], file_text)

            if author:
                author = author.group('author')
            if translator:
                translator = translator.group('translator')
            if illustrator:
                illustrator = illustrator.group('illustrator')

            # print out document metadata details
            print "***" * 25
            print "Here is the info for file {}".format(file_name)
            print "The title of the text is {}".format(title)
            print "The author is {}".format(author)
            print "The translator is {}".format(translator)
            print "The illustrator is {} \n".format(illustrator)

            # print the details of the count of the keywords by calling the keywordCount function
            keywordCount(keywords, file_text)


# call the main function
if __name__ == "__main__":
    # set the directory path
    directory = sys.argv[1]
    # assign the user specified keywords to be search for
    keywords = sys.argv[2:]

    # generate the regex patterns for keywords
    keywordPatterns(keywords)

    # iterate through files in directory and print results to the terminal
    getFiles(directory)