def merge_two_sorted_ascending_list(A, B):
    m = len(A)
    n = len(B)
    A = zeropad(A, n)
    last, i, j = m + n - 1, m - 1, n - 1

    while i >= 0 and j >= 0:
        if A[i] > B[j]:
            A[last] = A[i]
            last, i = last - 1, i - 1
        else:
            A[last] = B[j]
            last, j = last - 1, j - 1

    while j >= 0:
        A[last] = B[j]
        last, j = last - 1, j - 1
    print A


def merge_two_sorted_descending_list(A, B):
    m = len(A)
    n = len(B)
    A = zeropad(A, n)
    last, i, j = m + n - 1, m - 1, n - 1
    while i >= 0 and j >= 0:
        if A[i] < B[j]:
            A[last] = A[i]
            last, i = last - 1, i - 1
        else:
            A[last] = B[j]
            last, j = last - 1, j - 1

    while j >= 0:
        A[last] = B[j]
        last, j = last - 1, j - 1
    print A[::-1]

def merge_two_sorted_ascending_descending_list(A, B):
    m = len(A)
    n = len(B)
    A = zeropad(A, n)
    last, i, j = m + n - 1, m - 1, 0
    while i >= 0 and j <= n - 1:
        if A[i] < B[j]:
            A[last] = B[j]
            last, j = last - 1, j + 1
        else:
            A[last] = A[i]
            last, i = last - 1, i - 1
    print A

def zeropad(A, size):
    A += [0] * size
    return A

merge_two_sorted_ascending_list([1, 3, 5], [4, 6, 7])
merge_two_sorted_descending_list([5, 3, 1], [7, 6, 4])
merge_two_sorted_ascending_descending_list([1, 4, 5], [7, 6, 4])