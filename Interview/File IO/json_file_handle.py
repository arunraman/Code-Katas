import json

your_json = '["foo", {"bar":["baz", null, 1.0, 2]}]'
parsed = json.loads(your_json)
print json.dumps(parsed, indent = 4, sort_keys= True)

#write to a file
with open('arun.json', 'w') as outfile:
    json.dump(parsed, outfile, indent = 4, sort_keys = True)


# read from a file
with open('arun.json', 'r') as infile:
    parsed = json.load(infile)
    for i in xrange(len(parsed)):
        print parsed[i]
    #print json.dumps(parsed, indent = 4, sort_keys= True)

python_object = {'some_text': 'my text',
                 'some_number': 12345,
                 'null_value': None,
             'some_list': [1,2,3]}

json_string = json.dumps(python_object)
