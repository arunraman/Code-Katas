list = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print [item for sublist in list for item in sublist]

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

print flatten_json({'x':1, 'y':1, 'z':{'a':1,'b':2}})