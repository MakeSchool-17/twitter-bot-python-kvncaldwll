import re
import string


source_text = open('/Users/keivnc/Documents/pride_prejudice.txt', encoding='utf8').read().split()

histogram = {}

def histogram(source_text):
    for word in source_text:
        if word not in histogram:
            add_word = re.sub(r"\W+", word)
            histogram[add_word] = 1
        else:
            add_word = re.sub(r"\W+", word)
            histogram[add_word] += 1

histogram(source_text)


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histogram[word]
