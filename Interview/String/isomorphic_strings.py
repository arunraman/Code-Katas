def isomorphic_string(str1, str2):
    if len(str1) != len(str2):
        return False
    return len(set(zip(str1, str2))) == len(set(str1)) == len(set(str2))

print isomorphic_string("foo", "boo")
