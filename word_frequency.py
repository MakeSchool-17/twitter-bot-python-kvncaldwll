import re
import operator
import string

source_text = open('/Users/keivnc/Documents/pride_prejudice.txt').read().split()

histo = {}


def histogram(source_text):
    for word in source_text:
        word = re.sub("[\,?!_.():;-]", " ", word)
        word = word.lstrip('\"')
        word = word.rstrip('\"')
        word = word.lstrip('\'')
        word = word.rstrip('\'')
        if word not in histo:
            histo[word] = 1
        else:
            histo[word] += 1
    sort_histo = sorted(histo.items(), key=operator.itemgetter(1))
    return sort_histo


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histo[word]

if __name__ == "__main__":
    print(histogram(source_text))
