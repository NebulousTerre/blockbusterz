import urllib2
import pprint

content = urllib2.urlopen("https://api.themoviedb.org/4/list/2/?api_key=a49c725845c9487dad1ee0e3748d6613").read()
# print content
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(content)
file2write=open("movielist2.json",'w')
file2write.write(content)
file2write.close()
