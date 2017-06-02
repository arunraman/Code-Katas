def remove_duplicates_sorted_array_allowed_once(A):
    i = 0
    for n in A:
        if i < 1 or n > A[i - 1]:
            A[i] = n
            i += 1
    print i , A[:i]


def remove_duplicates_sorted_array_allowed_twice(A):
    i = 0
    for n in A:
        if i < 2 or n > A[i - 2]:
            A[i] = n
            i += 1
    print i , A[:i]


# Difficult and confusing methods for the above
# Better avoid this..

# def remove_duplicates_sorted_array(A):
#     if len(A) == 0:
#         return 0
#     j = 0
#     for i in range(0, len(A)):
#         if A[i] != A[j]:
#             A[i], A[j + 1] = A[j + 1], A[i]
#             j = j + 1
#     print j + 1, A[:j+1]
#
#
#
# def remove_duplicates_sorted_array_allowed_twice_2(A):
#     if not A:
#         return 0
#     last = 0; i = 1; same = False
#     while i < len(A):
#         if A[last] != A[i] or not same:
#             same = A[last] == A[i]
#             last += 1
#             A[last] = A[i]
#         i += 1
#     print last + 1, A[:last+1]


# Where the integers range from 1 <= a[i] <= n (n = size of array)
# Will not work for any random array, for any random array use dict method
def remove_all_duplicates_in_array(A):
    res = []
    for x in A:
        if A[abs(x) - 1] < 0:
            res.append(abs(x))
        else:
            A[abs(x) - 1] *= -1
    print res


def remove_all_duplicates_in_any_array(A):
    seen = set()
    uniq = [x for x in A if x not in seen and not seen.add(x)]
    print uniq


def removeElement(array, element):
    if (len(array) == 1 and array[0] == element) or (len(array) < 1):
        return []
    array = [x for x in array if x!= element]
    print array



#remove_duplicates_sorted_array([1, 1, 1, 2, 3])
remove_duplicates_sorted_array_allowed_once([1, 1, 1, 1 ,2, 3])
remove_duplicates_sorted_array_allowed_twice([1, 1, 1, 2, 2, 3, 3, 3, 3, 4])
#remove_duplicates_sorted_array_allowed_twice_2([1, 1, 1, 2, 2, 2, 3])
remove_all_duplicates_in_array([4,3,2,7,8,2,3,1,7])
remove_all_duplicates_in_any_array([4,3,100,7,150,2,3,1,7])
removeElement([1, 2, 3, 4, 5, 2, 2], 2)