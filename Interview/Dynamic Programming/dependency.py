def get_dependency(dependency_dict, k):
    dep = set()
    get_dependency_recursive(dependency_dict, k, dep)
    print dep

def get_dependency_recursive(dependency_dict, k, dep):
    if k not in dependency_dict:
        return
    elif k in dependency_dict:
        for v in dependency_dict[k]:
            get_dependency_recursive(dependency_dict, v, dep)
            dep.add(v)

dependency_dict = {'foo': ['bar', 'baz', 'goo'], 'bar' : ['boo'], 'baz': ['goo', 'a'], 'boo': ['b']}
get_dependency(dependency_dict, 'bar')