import time

def watch(fn, words):
    fp = open(fn, 'rw')
    while True:
        new = fp.readline()
        # Once all lines are read this just returns ''
        # until the file changes and a new line appears

        if new:
            #for word in words:
            #    if word in new:
            #       yield (new, word)
            yield new
        else:
            time.sleep(0.5)

fn = 'test.txt'
words = ['word']
for line in watch(fn, words):
    print line
#for hit_word, hit_sentence in watch(fn, words):
    #print "Found %r in line: %r" % (hit_word, hit_sentence)