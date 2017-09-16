# John,Smith,john.smith@gmail.com,Los Angeles,1
# ["John", "Smith", "john.smith@gmail.com", "Los Angeles", "1"]

# Jane,Roberts,janer@msn.com,"San Francisco, CA",0
# ["Jane", "Roberts", "janer@msn.com", "San Francisco, CA", "0"]

# "Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1
# ["Alexandra \"Alex\"", "Menendez", "alex.menendez@gmail.com", "Miami", "1"]

import re
class Solution(object):
    def parseCsv(self, sentence):
        result = []
        new_result = []
        sent_1 = list(sentence)
        new_str = ""
        new_w = ""

        for s in sent_1:
            if s != ',':
                new_str += " ".join(s)
            elif new_str:
                result.append(new_str)
                new_str = ""
        result.append(new_str)

        for i, w in enumerate(result):
            if w.startswith("\"") or w.endswith("\""):
                new_w += result[i]
                if new_w.startswith("\"") and new_w.endswith("\""):
                    #self.replace_two_double_quotes(new_w)
                    x = re.sub('\"{2}', '\\\"', new_w)
                    new_result.append(x)
                    new_w = ""
            else:
                new_result.append(w)
        return new_result

    def replace_two_double_quotes(self, new_sentence):
        x = list(new_sentence)
        i = 1
        while(i != len(x) - 2):
            if x[i] == x[i - 1] == "\"":
                print i
            i += 1


S = Solution()

print S.parseCsv('John,Smith,john.smith@gmail.com,Los Angeles,1')
print S.parseCsv('Jane,Roberts,janer@msn.com,"San Francisco, CA",0')
print S.parseCsv('"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1')