#https://urllib3.readthedocs.io/en/latest/

import urllib3 #anaconda lib NOT otherwise maybe
import json

http = urllib3.PoolManager()

lst = []
count = 0
for i in range(1,11):
    link = "https://api.themoviedb.org/4/discover/movie?primary_release_date.gte=1990-09-15&primary_release_date.lte=2017-10-22&page=" + str(i) + "&api_key=a49c725845c9487dad1ee0e3748d6613"
    r = http.request('GET',link)
    
    #Converted byte obj to dict obj. 
    dict = json.loads(r.data)
    #Got the list object from the dict
    movieList = dict['results']
    
    # looped through each dict in the List
    for movie in movieList:
        count=count+1
        #created a list from all the dicts appended
        lst.append(movie)
    # print()
    # lst.append(dict['results'])

print(lst)

#content = urllib3.urlopen("https://api.themoviedb.org/4/list/2/?api_key=a49c725845c9487dad1ee0e3748d6613").read()
