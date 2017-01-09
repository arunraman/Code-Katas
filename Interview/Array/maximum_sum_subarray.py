'''To find the maximum sum in an array of negative and
positive integers(kadane's algorithm)'''


def maximum_sum_subarray(array):
    if len(array) < 2:
        return array
    current_sum = 0
    current_index = -1
    best_sum = 0
    best_start_index = -1
    best_end_index = -1
    all_negative = True

    for i in xrange(len(array)):
        val = current_sum + array[i]
        if val > 0:
            if current_sum == 0:
                current_index = i
            current_sum = val
            all_negative = False
        else:
            current_sum = 0

        if current_sum > best_sum:
            best_sum = current_sum
            best_start_index = current_index
            best_end_index = i

    if all_negative:
        best_sum = max(array)
        best_start_index = best_end_index = array.index(best_sum)

    return array[best_start_index:best_end_index + 1], best_sum


def Main():
    a = [-5, -2, -3, -3, -5]
    b = [5, 2, -3, -11, 18, 1]
    c = [-4, 4, -3, 3, -2, 2]
    d = [4, 5, -9]
    e = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
    f = [1, 2, 3, 4, 5, -20, 10]

    print maximum_sum_subarray(a)
    print maximum_sum_subarray(b)
    print maximum_sum_subarray(c)
    print maximum_sum_subarray(d)
    print maximum_sum_subarray(e)
    print maximum_sum_subarray(f)

if __name__ == '__main__':
    Main()
