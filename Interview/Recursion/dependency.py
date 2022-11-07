def get_dependency(dependency_dict, k):
    dep = set()
    tracking = set()
    get_dependency_recursive(dependency_dict, k, dep, tracking)
    print list(dep)


def get_dependency_recursive(dependency_dict, k, dep, tracking):
    if k not in dependency_dict or k in tracking:
        return
    elif k in dependency_dict:
        tracking.add(k)
        for v in dependency_dict[k]:
            get_dependency_recursive(dependency_dict, v, dep, tracking)
            dep.add(v)


dependency_dict = {'foo': ['bar', 'baz', 'goo'],
                   'bar': ['boo'], 'baz': ['goo', 'a'], 'boo': ['b']}
get_dependency(dependency_dict, 'foo')
