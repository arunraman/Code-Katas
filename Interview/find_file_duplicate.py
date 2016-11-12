#
# input: '/foo/'
# output:
# [
#    ['/foo/bar.png', '/foo/images/foo.png'],
#    ['/foo/file.tmp', '/foo/other.temp', '/foo/temp/bar/that.foo']
# ]

# /foo/temp/bar/that.foo



import os, hashlib
from collections import defaultdict


def findDup(root):
    dict = defaultdict(list)
    file_size_dict = defaultdict(list)
    result = []
    for dir_name, sub_dir_name, file_name_list in os.walk(root):
        for i in file_name_list:
            file_path = os.path.join(dir_name, i)
            _size = os.path.getsize(file_path)
            file_size_dict[_size].append(file_path)
    for file_size, file_name_list in file_size_dict.iteritems():
        if len(file_name_list) > 1:
            for _file in file_name_list:
                hash_sum = get_hash_sum(_file)
                if hash_sum in dict:
                    dict[hash_sum].append(_file)
                else:
                    dict[hash_sum] = [_file]
        else:
            result.append((file_name_list[0]))
    for key, value in dict.iteritems():
        result.append(value)
    print result


def get_hash_sum(file_path, BLOCK_SIZE=65536):
    with open(file_path, 'rb') as F:
        _buf = F.read(BLOCK_SIZE)
        hash_sum = hashlib.md5()
        while (len(_buf) > 0):
            hash_sum.update(_buf)
            _buf = F.read(BLOCK_SIZE)
        F.close()
    #print (hash_sum.hexdigest())
    return hash_sum


def Main():
    root_path = '/tmp/arun'
    if os.path.exists(root_path):
        findDup(root_path)

Main()