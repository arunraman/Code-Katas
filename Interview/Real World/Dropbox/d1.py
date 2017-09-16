#
# input: '/foo/'
# output:
# [
#    ['/foo/bar.png', '/foo/images/foo.png'],
#    ['/foo/file.tmp', '/foo/other.temp', '/foo/temp/bar/that.foo']
# ]

# /foo/temp/bar/that.foo



# Approach for the question

# Will build a sizing bucket and any size key that has more than one
# file will go and run a hash on the entire file.
# Will iterate through the hash sum dictionary and any hash value
# that has more than one file path is a duplicate and will be
# added to the file_duplicate_list array

# Clarification
# is the files system mounted or not ?
# if mounted via nfs or something else we need to take into concern about the i/o

# Are there Symlinks ?
# For any symlink file, they will be added to the same size key in the size dictionary
# but we don't need to calculate the hash as it is repetitive. so we will add it to another bucket
# and add it  the result along with the parent files. if the parent files are in the same root path.

# eg the baz -> bar and bar is inside the /foo/bar, soft_1 - > /goo/real, soft_2 -> /goo/real

# Are there Hardlinks ?
# Hardlinks and circular hardlinks have

# This will not cover this test case where A hardlink/softlink file from some other directory
# is copied



from collections import defaultdict
import os
import hashlib

class Solution(object):
    def __init__(self):
        self.list_of_files = []
        self.directory_entries = []
        self.files_by_size = defaultdict(list)
        self.files_by_hash_sum = defaultdict(list)
        self.files_by_symlink = defaultdict(list)
        self.files_by_hardlink_inode = defaultdict(list)
        self.file_duplicate_list = []

    def find_duplicates(self, root_path):

        ''' This solution first separates by file size, then does a second pass by SHA256 hash '''
        self.list_of_files = [root_path]
        self.group_files_by_size()
        self.group_files_by_hash()
        return self.group_all_duplicates()

    def group_files_by_size(self):
        # Iteratively depth-first traverse root_path
        while self.list_of_files:
            directory = self.list_of_files.pop()

            for dir_entry in os.listdir(directory):
                dir_entry = os.path.join(directory, dir_entry)
                self.directory_entries.append(dir_entry)
                if os.path.isdir(dir_entry):
                    self.list_of_files.append(dir_entry)
                else:
                    size = os.stat(dir_entry).st_size
                    if os.path.islink(dir_entry) or os.stat(dir_entry).st_nlink > 1:
                        if  os.stat(dir_entry).st_nlink > 1:
                            # hard links
                            self.get_parent_hard_linked_file_path(dir_entry,
                                                                  os.stat(dir_entry).st_ino)
                        else:
                            # soft links
                            self.get_parent_sym_linked_file_path(dir_entry)
                    else:
                        self.files_by_size[size].append(dir_entry)


    def get_parent_sym_linked_file_path(self, symlink_file):
        self.files_by_symlink[os.path.realpath(symlink_file)].append(symlink_file)

    def get_parent_hard_linked_file_path(self, hardlink_file, inode_number):
        self.files_by_hardlink_inode[inode_number].append(hardlink_file)

    def group_files_by_hash(self):
        # Now go through every size and verify sameness by hashing
        for size, filenames in self.files_by_size.iteritems():
            if len(filenames) > 1:
                for filename in filenames:
                    self.files_by_hash_sum[self.get_hash_sum(filename)].append(filename)

    def get_hash_sum(self, filename, BLOCK_SIZE=1024):
        hash_sum = hashlib.md5()
        with open(filename, 'rb') as f:
            while True:
                b = f.read(BLOCK_SIZE)
                if not b:
                    break
                hash_sum.update(b.encode())
        f.close()
        return hash_sum.digest()


    def group_all_duplicates(self):
        # Add all the hard link files
        for filenames in self.files_by_hardlink_inode.values():
            if len(filenames) > 1:
                self.file_duplicate_list.append(filenames)

        # Now go through all the same hashes and print them
        for filenames in self.files_by_hash_sum.values():
            if len(filenames) > 1:# or filename in self.files_by_symlink:
                temp = []
                for filename in filenames:
                    if filename in self.files_by_symlink:
                        temp.append(filename)
                        temp.extend(self.files_by_symlink[filename])
                        del self.files_by_symlink[filename]
                    else:
                        temp.append(filename)
                self.file_duplicate_list.append(temp)

        # if there are multiple symlink files, which are duplicate and the parent file is in another directory.
        # Then we need to get the symlink files alone

        for parent_file, filenames in self.files_by_symlink.iteritems():
            temp = []
            if parent_file in self.directory_entries:
                temp.append(parent_file)
            temp.extend(filenames)
            self.file_duplicate_list.append(temp)

        # for filename in self.files_by_symlink.keys():
        #     temp = []
        #     if filename in self.directory_entries:
        #         temp.append(filename)
        #     elif len(self.files_by_symlink[filename]) > 1:
        #         temp.extend(self.files_by_symlink[filename])
        #
        #     if temp:
        #         self.file_duplicate_list.append(temp)
        return self.file_duplicate_list



S = Solution()
x = S.find_duplicates('/Users/aruraman/foo')
#print x
print str(x).replace(', [',"\n\n [")
