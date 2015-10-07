
hashtable = ['red', 1, 'fish', 4, 'blue', 1, 'one', 1, 'two', 1]


def add_item(key, value):
    hashtable.extend([key, value])
    print("key: " + key + " value: " + str(value) + " added.")


def find_value(key):
    value = None
    for index, item in enumerate(hashtable):
        if key == item:
            value = hashtable[index + 1]
            break
    print("key: " + key + " value: " + str(value))
    return value


def update_value(key, number):
    value = None
    for index, item in enumerate(hashtable):
        if key == item:
            value = hashtable[index + 1] = number
            break
    print("value for key: " + key + " updated.")
    return value


def all_keys():
    print("keys: " + str(hashtable[::2]))


def all_values():
    print("values: " + str(hashtable[1::2]))
