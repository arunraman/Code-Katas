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


S = Solution()

print S.parseString('SELECT * FROM table WHERE name LIKE "Aaron;"; SELECT * FROM table2 WHERE name2 = "Arun";')