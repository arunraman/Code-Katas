import string_questions
import random
'''
Generate 10char alphanumeric token
'''
print ''.join(random.choice(string_questions.ascii_letters + string_questions.digits)
              for i in xrange(10))
