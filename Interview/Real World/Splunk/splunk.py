# // Black box helper function that tells you whether a given character is part of a word
# // iswordchar('!') == false
# // iswordchar('\'') == true
# // iswordchar('H') == true
# // iswordchar(' ') == false
# static bool iswordchar(char c);


# // Viewing the string as a sentence, reverse the words within the string
# // input:  "  Hello it's dev at   Spl!unk!!"
# // output: "  olleH s'ti ved ta   knulpS!!"
                                    #lpS!knu!!
# static void reversewords(char *s)
# {

# }

class Solution(object):
    def reverseString(self, strs):
        result = ""
        temp_str = ""
        for char in list(strs):
            if self.iswordchar(char):
                temp_str += char # s'ti #Hello
            else:
                result += temp_str[::-1] #lpS! #Knu #s'ti elloH
                result += char #Spl! #Knu!!
                temp_str = ""  # ""
        return result

    def iswordchar(self, char):
        if char == "!" or char == " ":
            return False
        else:
            return True

S = Solution()
print S.reverseString("  Hello it's dev at   Spl!unk!!")