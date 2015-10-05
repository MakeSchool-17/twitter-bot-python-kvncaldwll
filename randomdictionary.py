import random
import sys

dict_file = open('/usr/share/dict/words').read().splitlines()


if __name__ == "__main__":
    # turn into integer
    user_num = int(sys.argv[1])
    # select amount of words = to integer
    for i in range(0, user_num):
        # random index number from dict file
        rand_words = random.randint(0, len(dict_file) - 1)
        # print single line
        sys.stdout.write(dict_file[rand_words] + ' ')
    # line break
    sys.stdout.write('\n')
