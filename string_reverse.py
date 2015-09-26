import sys


if __name__ == "__main__":
    word_list = sys.argv[1:]
    word_list.reverse()
    if len(word_list) <= 1:
        reversed_word = word_list[0][::-1]
        print(reversed_word)
    else:
        final_reverse = ' '.join(word_list)
        print(final_reverse)

