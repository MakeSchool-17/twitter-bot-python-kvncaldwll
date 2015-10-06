# import sys

# text source file
source_text = open('/Users/keivnc/Documents/pride_prejudice.txt').read().split()


# histogram of unique words
def histogram(source_text):
    histogram = {}
    for word in source_text:
        # remove special characters
        word.replace('--', ' ')
        word = word.lstrip('\W, \d')
        word = word.rstrip('\W, \d')
        # if doesnt exist add and start counter
        if word not in histogram:
            histogram[word] = 1
        # if does exist add 1 to counter
        else:
            histogram[word] += 1
    return(histogram)


def unique_words(histogram):
    total_words = histogram(source_text)
    print(len(total_words))


def frequency(histogram, word):
    word_list = histogram(source_text)
    print(word_list[word])
