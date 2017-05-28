import requests, json
response = requests.get("http://api.open-notify.org/iss-now.json")
print response

base_url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
address = raw_input()
address = address.replace(" ", "+")
key = 'AIzaSyAJ4iTlL_MwG5NYR6ion0vfuAT-kWx3Ci8'
uri = base_url + str(address) + '&key=' + key
response = requests.post(uri)
r = response.json()
print r['results']