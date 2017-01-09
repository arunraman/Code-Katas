def SortCount(A):
    l = len(A)
    if l > 1:
        n = l // 2
        C = A[:n]
        D = A[n:]
        C, c = SortCount(A[:n])
        D, d = SortCount(A[n:])
        B, b = MergeCount(C, D)
        return B, b + c + d
    else:
        return A, 0

def MergeCount(A, B):
    count = 0
    M = []
    while A and B:
        if A[0] <= B[0]:
            M.append(A.pop(0))
        else:
            count += len(A)
            M.append(B.pop(0))
    M += A + B
    return M, count


# Better Solution above with count

# def merge_sort(lst):
#     """Sorts the input list using the merge sort algorithm.
#
#     """
#     if len(lst) <= 1:
#         return lst
#     mid = len(lst) // 2
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return merge(left, right)
#
# def merge(left, right):
#     """Takes two sorted lists and returns a single sorted list by comparing the
#     elements one at a time.
#
#     """
#     if not left:
#         return right
#     if not right:
#         return left
#     if left[0] < right[0]:
#         return [left[0]] + merge(left[1:], right)
#     return [right[0]] + merge(left, right[1:])




print SortCount([4, 5, 1, 6, 3])
