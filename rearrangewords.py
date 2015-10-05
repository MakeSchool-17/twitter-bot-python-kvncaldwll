import sys
import random

if __name__ == "__main__":
    user_input = sys.argv[1:]
    if len(user_input) == 1:
        rev = ''.join(user_input)
        print(rev[::-1])
        rand = ''.join(random.sample(user_input[0], len(user_input[0])))
        print(rand)
    else:
        # print reversed
        print(' '.join(user_input[::-1]))
        # print shuffled
        random.shuffle(user_input)
        print(' '.join(user_input))
import sys
from random import shuffle

if __name__ == "__main__":
    user_input = sys.argv[1:]
    shuffle(user_input)
    print(user_input)
