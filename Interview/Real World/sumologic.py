def tableify(names, columns):
    rows = int(len(names) / columns) + (len(names) % columns > 0)
    result = [[] for _ in range(rows)]

    for i in xrange(len(names)):
        result[i % rows].append(names[i])
    return result


names = 'Adam Brett Cari Donna Ethan Fred Grok Han Izzy Jay'.split()
columns = 4

print str(tableify(names, columns)).replace(', [',",\n [")

# Question:

# Given a string, find the longest substring that doesnt contain any repeating characters.
# abaded - bade

# aaaaa - a


def lengthOfLongestSubstring(S):
    # This should be replaced by an array (size = alphabet size).
    last_occurrence = {}
    longest_len_so_far = 0
    longest_pos_so_far = 0
    curr_starting_pos = 0
    curr_length = 0

    for k, c in enumerate(S):
        l = last_occurrence.get(c, -1)
        # If no repetition within window, no problems.
        if l < curr_starting_pos:
            curr_length += 1
        else:
            # Check if it is the longest so far
            if curr_length > longest_len_so_far:
                longest_pos_so_far = curr_starting_pos
                longest_len_so_far = curr_length
            # Cut the prefix that has repetition
            curr_length -= l - curr_starting_pos
            curr_starting_pos = l + 1
        # In any case, update last_occurrence
        last_occurrence[c] = k

    # Maybe the longest substring is a suffix
    if curr_length > longest_len_so_far:
        longest_pos_so_far = curr_starting_pos
        longest_len_so_far = curr_length

    return S[longest_pos_so_far:longest_pos_so_far + longest_len_so_far]


print lengthOfLongestSubstring("abadedaa")
print lengthOfLongestSubstring("aaaaa")
print lengthOfLongestSubstring("abcabc")

