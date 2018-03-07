# Name Matching
#
#   At Checkr, one of the most important aspects of our work is accurately matching records
# to candidates. One of the ways that we do this is by comparing the name on a given record
# to a list of known aliases for the candidate. In this exercise, we will implement a
# `name_match` method that accepts the list of known aliases as well as the name returned
# on a record. It should return True if the name matches any of the aliases and False otherwise.
#
# The name_match method will be required to pass the following tests:
#
# 1. Exact match
#
#   known_aliases = ['Alphonse Gabriel Capone', 'Al Capone']
#   name_match(known_aliases, 'Alphonse Gabriel Capone') => True
#   name_match(known_aliases, 'Al Capone')               => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => False
#
#
# 2. Middle name missing (on alias)
#
#   known_aliases = ['Alphonse Capone']
#   name_match(known_aliases, 'Alphonse Gabriel Capone') => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => True
#   name_match(known_aliases, 'Alexander Capone')        => False
#
#
# 3. Middle name missing (on record name)
#
#   known_aliases = ['Alphonse Gabriel Capone']
#   name_match(known_aliases, 'Alphonse Capone')         => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => False
#   name_match(known_aliases, 'Alexander Capone')        => False
#
#
# 4. More middle name tests
#    These serve as a sanity check of your implementation of cases 2 and 3
#
#   known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone']
#   name_match(known_aliases, 'Alphonse Gabriel Capone') => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => True
#   name_match(known_aliases, 'Alphonse Edward Capone')  => False
#
#
# 5. Middle initial matches middle name
#
#   known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']
#   name_match(known_aliases, 'Alphonse G Capone')       => True
#   name_match(known_aliases, 'Alphonse Francis Capone') => True
#   name_match(known_aliases, 'Alphonse E Capone')       => False
#   name_match(known_aliases, 'Alphonse Edward Capone')  => False
#   name_match(known_aliases, 'Alphonse Gregory Capone') => False
#
#
# Bonus: Transposition
#
# Transposition (swapping) of the first name and middle name is relatively common.
# In order to accurately match the name returned from a record we should take this
# into account.
#
# All of the test cases implemented previously also apply to the transposed name.
#
#
# 6. First name and middle name can be transposed
#
#   'Gabriel Alphonse Capone' is a valid transposition of 'Alphonse Gabriel Capone'
#
#   known_aliases = ['Alphonse Gabriel Capone']
#   name_match(known_aliases, 'Gabriel Alphonse Capone') => True
#   name_match(known_aliases, 'Gabriel A Capone')        => True
#   name_match(known_aliases, 'Gabriel Capone')          => True
#   name_match(known_aliases, 'Gabriel Francis Capone')  => False
#
#
# 7. Last name cannot be transposed
#
#   'Alphonse Capone Gabriel' is NOT a valid transposition of 'Alphonse Gabriel Capone'
#   'Capone Alphonse Gabriel' is NOT a valid transposition of 'Alphonse Gabriel Capone'
#
#   known_aliases = ['Alphonse Gabriel Capone']
#   name_match(known_aliases, 'Alphonse Capone Gabriel') => False
#   name_match(known_aliases, 'Capone Alphonse Gabriel') => False
#   name_match(known_aliases, 'Capone Gabriel')          => False

def name_match(known_aliases, record_name):
    # Implement me
    if record_name in known_aliases:
        return True
    elif __middle_name_missing_record_name(record_name) in known_aliases:
        return True
    elif record_name in __middle_name_missing_alias_name(known_aliases):
        return True
    elif record_name in __middle_initial_aliases(known_aliases):
        return True
    elif len(record_name) == 3 and (__middle_initial_record_name(record_name) in __middle_initial_aliases(known_aliases)
                                    or record_name in __middle_initial_aliases(known_aliases)):
        return True
    else:
        return False


def __middle_name_missing_record_name(record_name):
    temp = record_name.split()
    first_name, last_name = temp[0], temp[-1]
    modified_rec_name = first_name + " " + last_name
    return modified_rec_name


def __middle_name_missing_alias_name(known_aliases):
    modified_known_aliases = []
    for alias in known_aliases:
        modified_alias_name = ""
        temp = alias.split()
        first_name, last_name = temp[0], temp[-1]
        modified_alias_name = first_name + " " + last_name
        modified_known_aliases.append(modified_alias_name)
        modified_known_aliases.append(alias)
    return modified_known_aliases


def __middle_initial_aliases(known_aliases):
    modified_known_aliases = []
    for alias in known_aliases:
        modified_alias_name = ""
        temp = alias.split()
        first_name, middle_initial, last_name = temp[0], temp[1][:1], temp[-1]
        modified_alias_name = first_name + " " + middle_initial + " " + last_name
        modified_known_aliases.append(modified_alias_name)
        modified_known_aliases.append(alias)
    return modified_known_aliases

def __middle_initial_record_name(record_name):
    temp = record_name.split()
    first_name, middle_initial, last_name = temp[0], temp[1][:1], temp[-1]
    modified_rec_name = first_name + " " + middle_initial + " " + last_name
    return modified_rec_name


### Tests ###

def assert_equal(expected, result, error_message):
    if expected != result:
        print(error_message)
        print('expected: %s' % expected)
        print('actual: %s' % result)
        print('')


def run_tests():
    # 1
    known_aliases = ['Alphonse Gabriel Capone', 'Al Capone']
    assert_equal(True, name_match(known_aliases, 'Alphonse Gabriel Capone'), 'error 1')
    assert_equal(True, name_match(known_aliases, 'Al Capone'), 'error 2')
    assert_equal(False, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 3')

    # 2
    known_aliases = ['Alphonse Capone']
    assert_equal(True, name_match(known_aliases, 'Alphonse Gabriel Capone'), 'error 4')
    assert_equal(True, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 5')
    assert_equal(False, name_match(known_aliases, 'Alexander Capone'), 'error 6')

    # 3
    known_aliases = ['Alphonse Gabriel Capone']
    assert_equal(True, name_match(known_aliases, 'Alphonse Capone'), 'error 7')
    assert_equal(False, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 8')
    assert_equal(False, name_match(known_aliases, 'Alphonse Edward Capone'), 'error 9')

    # 4
    known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone']
    assert_equal(True, name_match(known_aliases, 'Alphonse Gabriel Capone'), 'error 10')
    assert_equal(True, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 11')
    assert_equal(False, name_match(known_aliases, 'Alphonse Edward Capone'), 'error 12')

    # 5
    known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']
    assert_equal(True, name_match(known_aliases, 'Alphonse G Capone'), 'error 13')
    assert_equal(True, name_match(known_aliases, 'Alphonse Francis Capone'), 'error 14')
    assert_equal(False, name_match(known_aliases, 'Alphonse E Capone'), 'error 15')
    assert_equal(False, name_match(known_aliases, 'Alphonse Edward Capone'), 'error 16')
    assert_equal(False, name_match(known_aliases, 'Alphonse Gregory Capone'), 'error 17')

    # 6
    known_aliases = ['Alphonse Gabriel Capone']
    assert_equal(True, name_match(known_aliases, 'Gabriel Alphonse Capone'), 'error 18')
    assert_equal(True, name_match(known_aliases, 'Gabriel A Capone'), 'error 19')
    assert_equal(True, name_match(known_aliases, 'Gabriel Capone'), 'error 20')
    assert_equal(False, name_match(known_aliases, 'Gabriel Francis Capone'), 'error 21')

    # 7
    known_aliases = ['Alphonse Gabriel Capone']
    assert_equal(False, name_match(known_aliases, 'Alphonse Capone Gabriel'), 'error 22')
    assert_equal(False, name_match(known_aliases, 'Capone Alphonse Gabriel'), 'error 23')
    assert_equal(False, name_match(known_aliases, 'Capone Gabriel'), 'error 24')

    print('Test run finished')


if __name__ == "__main__":
    run_tests()