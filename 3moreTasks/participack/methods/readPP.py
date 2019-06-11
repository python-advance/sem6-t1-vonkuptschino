import json

# Make it work for Python 2+3 and with Unicode
import io

def readPP():
	try:
	    to_unicode = unicode
	except NameError:
	    to_unicode = str

	# Define data
	data = {'a list': [1, 42, 3.141, 1337, 'help', u'€'],
	        'a string': 'bla',
	        'another dict': {'foo': 'bar',
	                         'key': 'value',
	                         'the answer': 42}}
	# Read JSON file
	with open('data.json') as data_file:
	    data_loaded = json.load(data_file)
