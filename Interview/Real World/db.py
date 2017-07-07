import os, hashlib
from collections import defaultdict

class Solution(object):
    def __init__(self):
        self.list_of_files = []
        self.directory_entries = []
        self.files_by_size = defaultdict(list)
        self.files_by_hash_sum = defaultdict(list)
        self.file_duplicate_list = []

    def find_duplicates(self, root_path):

        self.list_of_files = [root_path]
        self.group_files_by_size()
        self.group_files_by_hash()
        self.group_all_duplicates()
        return self.file_duplicate_list

    def group_files_by_size(self):
        # Iteratively depth-first traverse root_path
        while self.list_of_files:
            directory = self.list_of_files.pop()
            self.directory_entries = os.listdir(directory)
            for dir_entry in self.directory_entries:
                dir_entry = os.path.join(directory, dir_entry)
                if os.path.isdir(dir_entry):
                    self.list_of_files.append(dir_entry)
                else:
                    size = os.stat(dir_entry).st_size
                    self.files_by_size[size].append(dir_entry)

    def group_files_by_hash(self):
        # Now go through every size and verify sameness by hashing
        for filenames in self.files_by_size.values():
            if len(filenames) > 1:
                for filename in filenames:
                    self.files_by_hash_sum[self.get_hash_sum(filename)].append(filename)

    def group_all_duplicates(self):
        # Now go through all the same hashes and print them
        for filenames in self.files_by_hash_sum.values():
            if len(filenames) > 1:
                self.file_duplicate_list.append(filenames)

    def get_hash_sum(self, filename, BLOCK_SIZE = 1024, LIMIT_SIZE = None):
        hash_sum = hashlib.md5()
        try:
            F = open(filename, "rb")
        except IOError:
            return None
        if LIMIT_SIZE:
            chunk = F.read(LIMIT_SIZE)
            hash_sum.update(chunk.encode())
        else:
            while True:
                chunk = F.read(BLOCK_SIZE)
                if not chunk:
                    break
                hash_sum.update(chunk.encode())
        F.close()
        return hash_sum.digest()


S = Solution()
x = S.find_duplicates('/Users/aruraman/foo')
#print x
print str(x).replace(', [',"\n\n [")