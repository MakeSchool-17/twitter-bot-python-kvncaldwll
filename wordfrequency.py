# import sys

# text source file
source_text = open('/Users/keivnc/Documents/pride_prejudice.txt').read().split()


# histogram of unique words
#def histogram(source_text):
#    histogram = {}
#    for word in source_text:
#        # remove special characters
#        word.replace('--', ' ')
#        word = word.lstrip('\W, \d')
#        word = word.rstrip('\W, \d')
#        # if doesnt exist add and start counter
#        if word not in histogram:
#            histogram[word] = 1
#        # if does exist add 1 to counter
#        else:
#            histogram[word] += 1
#    return(histogram)


# histogram using nested lists
def histogram(source_text):
    histogram = []
    clean_word_list = purify_words(source_text)
    # looks if words match in histogram
    for word in clean_word_list:
        if histogram_match(histogram, word) is None:
            histogram.append([word, 1])
    return histogram


def unique_words(histogram):
    total_words = histogram(source_text)
    print(len(total_words))


def frequency(histogram, word):
    word_list = histogram(source_text)
    print(word_list[word])


def purify_words(source_text):
    clean_word_list = []
    for word in source_text:
        # remove special characters-ish
        word.replace('--, _', ' ')
        word = word.lstrip('\W, \d')
        word = word.rstrip('\W, \d')
        clean_word_list.append(word)
    return clean_word_list


# check if word matching any nested list index
def histogram_match(histogram, word):
    for item in histogram:
        if word == item[0]:
            item[1] += 1
            return item
    return None

