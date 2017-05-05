import random

BASE_ALPH = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
BASE_DICT = dict((c, v) for v, c in enumerate(BASE_ALPH))
BASE_LEN = len(BASE_ALPH)


def base_decode(string):
    num = 0
    for char in string:
        num = num * BASE_LEN + BASE_DICT[char]
    return num


def base_encode(num):
    if not num:
        return BASE_ALPH[0]

    encoding = ""
    while num:
        num, rem = divmod(num, BASE_LEN)
        encoding = BASE_ALPH[rem] + encoding
    return encoding

if __name__ == '__main__':
    url = "http://dealnews.com/"
    tiny_url = "http://tinyurl.com/"
    id = random.randint(0, 1000)
    encoded_id = base_encode(id)

    print encoded_id
    decoded_id = base_decode(encoded_id)
    print decoded_id
