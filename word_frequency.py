import re

source_text = open('/Users/keivnc/Documents/pride_prejudice.txt').read().split()

histo = {}


def histogram(source_text):
    for word in source_text:
        if word not in histo:
            add_word = re.sub(r"\W+", "", word)
            histo[add_word] = 1
        else:
            add_word = re.sub(r"\W+", "", word)
            histo[add_word] += 1

    return histo


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histo[word]

if __name__ == "__main__":
    print(histogram(source_text))
