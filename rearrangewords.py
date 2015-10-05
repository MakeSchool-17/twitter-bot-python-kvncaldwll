import sys
import random

if __name__ == "__main__":
    user_input = sys.argv[1:]
    # for single word input
    if len(user_input) == 1:
        rev = ''.join(user_input)
        # reverse string
        print(rev[::-1])
        # randomize string
        rand = ''.join(random.sample(user_input[0], len(user_input[0])))
        print(rand)
    # for multiple word input
    else:
        # print reversed list / reversed word order
        print(' '.join(user_input[::-1]))
        # print shuffled list / random word order
        random.shuffle(user_input)
        print(' '.join(user_input))
