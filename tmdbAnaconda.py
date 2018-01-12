#https://urllib3.readthedocs.io/en/latest/

import urllib3 #anaconda lib NOT otherwise maybe

http = urllib3.PoolManager()

r = http.request('GET',"https://api.themoviedb.org/4/list/2/?api_key=a49c725845c9487dad1ee0e3748d6613")
print(r.data)
