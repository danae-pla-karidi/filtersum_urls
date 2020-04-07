"""
Filters a file containing counted urls with a record list, counts 
the total number of occurrences of every record in the file with 
urls and stores them in 'output.csv'

"""

import sys
import csv 
import collections
set_urls = set(line.strip() for line in open(sys.argv[1]))
set_expanded = set(line.strip() for line in open(sys.argv[2]))
set_inter = set_expanded.intersection(set_urls) 
dataset=open("output.csv", 'w') 
fp= open(sys.argv[3])
lines = fp.readlines()
read_urls=open(sys.argv[4],'r') 
lineu=read_urls.readlines()
for min in lineu:	
	m=min.split() 
	mylist=[int("0")]
	for j in m: 
		if 	(j in set_inter): 
			for line in lines: 
				joo=line.split()
				if (joo[1] == j) or ((joo[1]+"/")==j):
					mylist.append(int(joo[0]))
	a=sum(mylist)					
	dataset.write(m[1]+"\t"+m[0]+"\t"+m[2]+"\t"+str(a)+'\n')
dataset.close()
fp.close()
read_urls.close()

