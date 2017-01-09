# Actual line by line content of a file "example.csv"
# "ColumnA", Column B
# # "a", b
# # c, ", d"
# # e, "\\\'t"
# # ", d", "\'t"

# Array of arrays of string to return
# [["ColumnA", "Column B"],
# # ["a", "b"],
# # ["c",  ", d"],
# ["e, "\'t"]]


def solution(str):
    result = []
    s_1 = str.splitlines()
    res = []
    for s_2 in s_1:
        s_3 = s_2.strip()
        for i in s_3.split(','):
            j = i.strip()
            c = list(i)
            if c[0] == "\"" and c[len(c) - 1] == "\"":
                res.append(j)
            else:
                res.append(j)
        result.append(res)
        res = []

    for x in result:
        print x


solution('''"ColumnA", Column B
         "a", b
         c, ", d"
         ", d", "\'t"''')
