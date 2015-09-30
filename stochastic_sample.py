import random
import sys

user_text = str(sys.argv[1:].pop())

source_text = open('/Users/keivnc/Documents/'+user_text).read().split()

histo = {}


def histogram(source_text):
    for word in source_text:
        word = word.replace("--", " ")
        word = word.rstrip('0123456789,?!_:;.-\"')
        word = word.lstrip('0123456789,?!_:;.-\"')
        if word not in histo:
            histo[word] = 1
        else:
            histo[word] += 1
    print(len(histo))
    return histo


def select_rand(histo):
    total = []
    i = 0
    for key, value in histo.items():
        while i < value:
            total.append(key)
            i += 1
        i = 0
    rand_select = random.randint(0, len(total) - 1)
    print(len(total))
    print(total[rand_select])

if __name__ == "__main__":
    histogram(source_text)
    select_rand(histo)
