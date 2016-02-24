from urllib2 import Request, urlopen
import json
import redis
import urlparse
import os
from StringIO import StringIO
import requests
from PIL import Image
from flask import send_file, Flask

app = Flask('MovieLocator')
with app.app_context():
    REDIS_URL = urlparse.urlparse(os.environ.get('REDISCLOUD_URL', 'redis://:@localhost:6379/'))
    r = redis.StrictRedis(
                host=REDIS_URL.hostname, port=REDIS_URL.port,
                password=REDIS_URL.password)

    class MovieInfo(object):
        def __init__(self, movie):
            self.movie_name = movie.replace(" ", "+")

        def get_movie_info(self):
            url = 'http://www.omdbapi.com/?t=' + self.movie_name + '&y=&plot=short&r=json'
            result = Request(url)
            response = urlopen(result)
            infoFromJson = json.loads(response.read())
            self._cache_image(infoFromJson)
            return infoFromJson

        def _cache_image(self, infoFromJson):
            key = "{}".format(infoFromJson['Title'])
            # Open redis.
            cached = r.get(key)
            if not cached:
                # Download the image.
                response = requests.get(infoFromJson['Poster'])
                image = Image.open(StringIO(response.content))
                r.setex(key, (60*60*5), image)
                return True
                # response = requests.get(infoFromJson['Poster'])
                # # Open the image.
                # output = StringIO(response.content)
                # r.setex(key, (60*60*5), output.getvalue())
                # output.close()
                # return True


        def get_image(self, key):
            cached = r.get(key)
            if cached:
                image = StringIO(cached)
                image.seek(0)
                return send_file(image, mimetype='image/jpg')


# if __name__ == '__main__':
#     M = MovieInfo("Furious 7")
#     M.get_movie_info()
#     M.get_image("Furious 7")