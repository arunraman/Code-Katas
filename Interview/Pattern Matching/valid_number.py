import re
def valid_number(string):
    print bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", string))
