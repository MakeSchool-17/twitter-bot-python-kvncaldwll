import random
import sys


if __name__ == "__main__":
    new_arr = sys.argv[1:]
    random.shuffle(new_arr)
    print(' '.join(new_arr))
