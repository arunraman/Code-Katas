
#string_list = ['foo','goo','boo','foo','loo', 'too']

#sorted_list = sorted(string_list, key=str.lower)

from collections import defaultdict

def arrange_bookshelf(bookshelf):
    index_map = defaultdict(list)
    book_position_tracker = 0
    for i in xrange(len(bookshelf)):
        index_map[bookshelf[i]].append(i)

    # for keys in sorted(index_map.keys()):
    #     for index_map[keys]



    print index_map


bookshelf = ['foo','goo','boo','foo','loo', 'too']

arrange_bookshelf(bookshelf)

