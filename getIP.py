import re
import sys
pattern =re.compile("\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}:80")
f=open("allIP.txt","w")


for i in range(1,1001):
	readfile="shodanPage_"+str(i)+".txt"
	for i, line in enumerate(open(readfile,"r")):
		for match in re.finditer(pattern, line):
			#print 'Found on line %s: %s' % (i+1, match.group(0))
			f.write(match.group(0).split(":")[0]+"\n")
			
f.close
			