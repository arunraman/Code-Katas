#
# SELECT * FROM table WHERE name LIKE "Aaron;"; SELECT * FROM table2 WHERE name2 = "Arun";
#
# [SELECT * FROM table WHERE name LIKE "Aaron;", SELECT * FROM table2 WHERE name2 = "Arun"]
#
# // Only double quotes
# // Double quotes can be escaped! "Aaron\""
#
#
class Solution(object):
    def parseString(self, sentence):
        result = []
        sent_1 = list(sentence)
        new_str = ""
        doublequotefound = False
        count = 0
        for s in sent_1:
            if s != ';' or doublequotefound:
                if s == "\"":
                    count += 1
                    doublequotefound = True
                    new_str += "\""
                    if count == 2:
                        doublequotefound = False
                        count = 0
                    continue
                else:
                    new_str += "".join(s)
            elif new_str:
                result.append(new_str)
                new_str = ""
        return result

    def split_line(self, line):
        n = len(line)
        i = 0
        in_quote = False
        token = ""
        result = list()
        while i < n:
            if in_quote:
                if line[i] == '"':
                    if i == n - 1:
                        result.append(token)
                        return "|".join(result)
                    elif line[i + 1] == '"':
                        token += line[i]
                        i += 1
                    else:
                        result.append(token)
                        token = ""
                        in_quote = False
                        i += 1
                else:
                    token += line[i]
            else:
                if line[i] == '"':
                    in_quote = True
                elif line[i] == ';':
                    result.append(token)
                    token = ""
                else:
                    token += line[i]
            i += 1
        if len(token) > 0:
            result.append(token)
        return '|'.join(result)



S = Solution()
print S.split_line('SELECT * FROM table WHERE name LIKE "Aaron;"; SELECT * FROM table2 WHERE name2 = "Arun";')