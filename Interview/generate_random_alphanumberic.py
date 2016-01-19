import string
import random
'''
Generate 10char alphanumeric token
'''
print ''.join(random.choice(string.ascii_letters + string.digits)
              for i in xrange(10))
