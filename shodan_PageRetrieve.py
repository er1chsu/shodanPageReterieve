import requests
import sys

for i in range(1,1001):
 url='https://www.shodan.io/search?query=dlink&page='+str(i)
 print str(i)
 print url 
 header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36','Cookie':' __cfduid=<your_cfduid_value>; polito=<your_polito_value>'}

 req=requests.get(url,headers=header)
 print "reponse "+str(req.status_code)
 if '200' not in str(req.status_code):
  print str(req.status_code)+" is not 200"
  sys.exit()
 saveName="shodanPage_"+str(i)+".txt"

 f = open(saveName,"w")
 f.write(req.text.encode('utf-8'))
 f.close

