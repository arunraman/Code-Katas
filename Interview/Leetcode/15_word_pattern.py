def wordPattern(pattern, str):
    s = pattern
    t = str.split()
    return len(
        set(zip(s, t))) == len(
        set(s)) == len(
        set(t)) and len(s) == len(t)

print wordPattern("abba", "dog cat cat dog")
