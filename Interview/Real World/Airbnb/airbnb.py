# John,Smith,john.smith@gmail.com,Los Angeles,1
# ["John", "Smith", "john.smith@gmail.com", "Los Angeles", "1"]

# Jane,Roberts,janer@msn.com,"San Francisco, CA",0
# ["Jane", "Roberts", "janer@msn.com", "San Francisco, CA", "0"]

# "Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1
# ["Alexandra \"Alex\"", "Menendez", "alex.menendez@gmail.com", "Miami", "1"]

class Solution(object):
    def parseCsv(self, sentence):
        result = []
        new_str = ""
        doublequotefound = False
        count = 0
        for char in list(sentence):
            if char != ',' or doublequotefound:
                if char == "\"":
                    count += 1
                    doublequotefound = True
                    new_str += "\""
                    if count == 2:
                        doublequotefound = False
                        count = 0
                    continue
                else:
                    new_str += "".join(char)
            elif new_str:
                result.append(new_str)
                new_str = ""
        result.append(new_str)
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
                elif line[i] == ',':
                    result.append(token)
                    token = ""
                else:
                    token += line[i]
            i += 1
        if len(token) > 0:
            result.append(token)
        return '|'.join(result)


S = Solution()

print S.split_line('John,Smith,john.smith@gmail.com,Los Angeles,1')
print S.split_line('Jane,Roberts,janer@msn.com,"San Francisco, CA",0')
print S.split_line('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1')