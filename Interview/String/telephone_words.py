#!/usr/bin/python
import random
tel_words = []

# Solution 1
# @return a list of strings, [s1, s2]


def letterCombinations(digits):
    if not digits:
        return []

    lookup = ["", "", "abc", "def", "ghi", "jkl", "mno",
                      "pqrs", "tuv", "wxyz"]
    result = [""]

    for digit in reversed(digits):
        choices = lookup[int(digit)]
        m, n = len(choices), len(result)
        result += [result[i % n] for i in xrange(n, m * n)]

        for i in xrange(m * n):
            result[i] += choices[i / n]

    return result

# Solution 2

keyboard = {
    '0': ['0', '0', '0'],
    '1': ['1', '1', '1'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
}


def getLetters(telephone_key, place):
    return keyboard[telephone_key][place]


def wordCombinations(telephone_number, curr_digit, result):
    if curr_digit == len(telephone_number):
        tel_words.append("".join(result))
        return

    if telephone_number[curr_digit] == "7" or \
            telephone_number[curr_digit] == "9":
        char = 4
    else:
        char = 3

    for i in xrange(char):
        result[curr_digit] = getLetters(telephone_number[curr_digit], i)
        wordCombinations(telephone_number, curr_digit + 1, result)


def telephoneWords(telephone_number):
    wordCombinations(telephone_number, 0,
                     [0 for i in xrange(len(telephone_number))])


def Main():
    tel_number = ""
    tel = tel_number.join(str(random.randint(2, 9)) for i in xrange(10))
    telephoneWords(tel)
    print len(letterCombinations(tel))
    # print tel_words
    print len(tel_words)


if __name__ == '__main__':
    Main()
