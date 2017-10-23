# Interview question
# Return a list of numbers that meet the following criteria
# A list of 1 - 10,000
# Each int in the index, when taken as seperate numbers and summed up is equal to 12.

# Example: the int 415 when broken apart is 4 + 1 + 5 = 10. 10 != 12
# However the int 534 when broken apart and summed is 5 + 3 + 4 = 12. so return 534.


def returnmatchinglist():
    matchinglist = []
    searchnumber = 12
    for i in range  (10000):
        j = list(map(int, str(i)))
        if 9 < i < 100:
            if j[0] + j[1] == searchnumber:
                matchinglist.append(i)
        elif 100 <= i < 1000:
            if j[0] + j[1] +j[2] == searchnumber:
                matchinglist.append(i)
        elif 1000 <= i < 10000:
            if j[0] + j[1] + j[2] + j[3] == searchnumber:
                matchinglist.append(i)
    return matchinglist

print(returnmatchinglist())
