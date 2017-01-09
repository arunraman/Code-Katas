from collections import defaultdict
CHUNK_LENGTH = 140
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
    PROMO_DICT[promo] = textwrap.wrap(line, 140)
    for k,v in PROMO_DICT.iteritems():
        for i in v:
            print i

def get_chunks_2(line, n):
    print(textwrap.fill(line, n))



if __name__ == '__main__':
    data = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. " \
           "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,"  \
           "when an unknown printer took a galley of type and scrambled it to make a type specimen book."  \
           "It has survived not only five centuries, but also the leap into electronic typesetting,"  \
           "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset"  \
           "sheets containing Lorem Ipsum passages, and more recently with desktop publishing software"  \
           "like Aldus PageMaker including versions of Lorem Ipsum."
    print get_chunks(data, "PROMO_1")
    print "\n\n\n\n"
    get_chunks_1(data, "PROMO_1")
    print "\n\n\n\n"
    get_chunks_2(data, 15)
