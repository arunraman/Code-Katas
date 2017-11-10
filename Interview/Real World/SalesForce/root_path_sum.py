#         8
#        / \
#       7   9
#      /  \ / \
#     12   19  6
#    /  \ /  \/ \
#   5    20  18  10
#
# Given a regular tree with a small modification: nodes can be shared. Example is shown above.
# Requirement: Write a function, check_sum(n), that take a number - n as input and return whether or
# not there is a branch in the tree that sums up to that number.
# If yes, print out that branch or branches (if more than one result).
# For example, with the tree above:
# check_sum(54)
# True, 8-7-19-20, 8-9-19-18
# check_sum(30)
# False, []
# check_sum(17)
# True or False

from collections import defaultdict, deque


class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        #self.left_parent = None
        #self.right_parent = None

class Solution(object):
    def __init__(self):
        self.root = root
        self.height = 0
        self.sum_result = []

    def check_sum(self, target, node):
        result = []
        #node = self.root
        #node_map = self.preprocessTree(node)
        # { '8': [7, 9]}

        if self.check_sum_recursive(node, target, result):
            print "True", self.sum_result
        else:
            print "False", self.sum_result

    def check_sum_recursive(self, node, target, result):
        if target == 0 and node.left == None and node.right == None:
            self.sum_result.append([result])  # self.sum_result = [[8 ,7, 19, 20]]
            result.pop()
        elif target != 0 and node.left == None and node.right == None:
            result.pop()
            return False
        result.append(node.value)  # result = [8 , 7 , 19]
        if node.value > 0:
            self.check_sum_recursive(node.left, target - node.value, result)
            self.check_sum_recursive(node.right, target - node.value, result)
        else:
            self.check_sum_recursive(node.left, target - (node.value * -1), result)
            self.check_sum_recursive(node.right, target - (node.value * -1), result)
        return True

    # def preprocessTree(self, node):
    #     node_list = []
    #     node_map = defaultdict(list)
    #     node_list.append(node)
    #     while (node_list != None):
    #         temp_node = node_list.pop()
    #         if temp_node.left_child:
    #             node_map[temp_node].append(temp_node.left_child)
    #         node_map[temp_node].append(temp_node.right_child)
    #         node_map[temp_node].append(temp_node.right_parent)
    #         node_map[temp_node].append(temp_node.left_parent)
    #
    #
    #     print node_map
    #     return node_map

S = Solution()
root = Node(8)