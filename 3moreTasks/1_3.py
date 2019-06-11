import requests #made with my fav lib
 
url = 'https://www.python.org/static/img/python-logo.png'
fileName = '/Users/vonkuptschino/Desktop/УЧЁБИЩЕ/2 курс/pythonist wannabe/5sem/PythonLogo.png'
req = requests.get(url)
file = open(fileName, 'wb')
for chunk in req.iter_content(100000):
    file.write(chunk)
file.close()
