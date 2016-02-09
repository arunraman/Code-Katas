CHUNK_LENGTH = 140


def get_chunks(line):
    line_length = len(line)
    if line_length < CHUNK_LENGTH:
        print [line]
    text_chunks = []
    while len(line) > CHUNK_LENGTH:
        raw_slice = line[:CHUNK_LENGTH]
        print raw_slice
        last_space = raw_slice.rfind(' ')
        # print last_space


def text_chunks(file):
    tweets = []
    with open(file) as F:
        lines = F.readlines()
        for line in lines:
            get_chunks(line.rstrip())


if __name__ == '__main__':
    text_chunks('data.txt')
