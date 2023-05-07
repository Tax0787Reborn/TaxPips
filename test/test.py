from urllib import request
download=lambda url,file:request.urlretrieve(url,file)
download('https://bootstrap.pypa.io/get-pip.py','get-pip.py')
