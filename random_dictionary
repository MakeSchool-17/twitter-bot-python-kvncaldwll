import random
import sys


if __name__ == "__main__":
    user_in = sys.argv[1:]
    convert_num = int(user_in.pop())
    with open('/usr/share/dict/words', encoding='utf8') as a_file:
        dict_list = list(a_file)
        out_list = []
        for i in range(convert_num):
            rand_num = random.randint(0, len(dict_list) - 1)
            word = dict_list[rand_num]
            out_list.append(word[0:len(word) - 1])
            final_out = ' '.join(out_list)
        sys.stdout.write(final_out)
