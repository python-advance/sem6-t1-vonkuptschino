import json

# Make it work for Python 2+3 and with Unicode
import io

def writePP():
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

	# Write JSON file
	with io.open('data.json', 'w', encoding='utf8') as outfile:
	    str_ = json.dumps(data,
	                      indent=4, sort_keys=True,
	                      separators=(',', ': '), ensure_ascii=False)
	    outfile.write(to_unicode(str_))

