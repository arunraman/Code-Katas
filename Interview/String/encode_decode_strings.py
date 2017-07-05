import random, string

class tinyURL(object):

    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(tinyURL.alphabet) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]

t = tinyURL()
t_url = t.encode("www.google.com")
print t_url
print t.decode(t_url)

class runLengthEncoding(object):
    def encode(self, text):
        if not text:
            return ""
        else:
            last_char = text[0]
            max_index = len(text)
            i = 1
            while i < max_index and last_char == text[i]:
                i += 1
            return last_char + str(i) + self.encode(text[i:])

    def decode(self, text):
        if not text:
            return ""
        else:
            char = text[0]
            quantity = text[1]
            return char * int(quantity) + self.decode(text[2:])


R = runLengthEncoding()
print R.encode("aaabbc")
print R.decode("a3b2c1")