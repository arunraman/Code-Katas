from collections import defaultdict
CHUNK_LENGTH = 25
PROMO_DICT = defaultdict(list)
import textwrap


def get_chunks(line, promo):
    i = 0
    j = 1
    while i < len(line):
        raw_slice = line[i:CHUNK_LENGTH * j]
        i += CHUNK_LENGTH
        j += 1
        PROMO_DICT[promo].append(raw_slice)
    return PROMO_DICT[promo]


def get_chunks_1(line, promo):
    PROMO_DICT[promo] = textwrap.wrap(line, CHUNK_LENGTH)
    for k, v in PROMO_DICT.iteritems():
      print v


if __name__ == '__main__':
    data = "Hi Sivasrinivas, your Uber is arriving now! And this is a bigger text"
    print get_chunks(data, "PROMO_1")
    print "\n\n\n\n"
    get_chunks_1(data, "PROMO_1")
