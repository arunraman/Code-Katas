from flask import Flask, render_template, request
from flask_googlemaps import GoogleMaps, Map
from MovieInfo import MovieInfo

app = Flask(__name__)
GoogleMaps(app)


@app.route("/", methods=['GET', 'POST'])
def mapview():
	movie_name = request.form.get('Movie')
	if request.method == 'POST' and movie_name != "":
		M = MovieInfo(movie_name)
		movie_dict = M.get_movie_info()
		image_file = M.get_image(movie_name)
		sndmap = Map(
			identifier="sndmap",
			lat=37.4419,
			lng=-122.1419,
			style="height:50%;width:50%;top:6000;left:1000;position:absolute;z-index:200",
			markers={'http://maps.google.com/mapfiles/ms/icons/green-dot.png': [(37.4419, -122.1419)],
			         'http://maps.google.com/mapfiles/ms/icons/blue-dot.png': [(37.4300, -122.1400)]}
		)
		return render_template('home.html', movie=movie_name, sndmap=sndmap, movie_info=movie_dict,
		                       image=image_file)
	else:
		return render_template('home.html', movie=movie_name)

if __name__ == "__main__":
	app.run(debug=True)
