import sys
from random import shuffle

if __name__ == "__main__":
    user_input = sys.argv[1:]
    shuffle(user_input)
    print(user_input)
