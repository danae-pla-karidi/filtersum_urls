import csv 
import collections

set_urls = set(line.strip() for line in open('publication_urls.csv')) #urls corresponding to publications
set_expanded = set(line.strip() for line in open('tweet_urls.txt')) #urls found in tweets with occurences counts
set_inter = set_expanded.intersection(set_urls) #urls that exist in both tweets and correspond to publications
dataset=open("output.csv", 'w') #output publication-->tweet count dataset

fp= open('tweet_urls.txt','r')
lines = fp.readlines()

read_urls=open('bip_data.csv','r') #records from bip: doi	pmc		pm 		url1	url2	....	urln	
lineu=read_urls.readlines()
dataset.write("doi"+"\t"+"pmc"+"\t"+"pm"+"\t"+ "count"+'\n')
for min in lineu:	#for every publication record sum the counter of their occurences in tweets
	m=min.split() 
	mylist=[int("0")]
	for j in m: #checks every available url for each publication
		if 	(j in set_inter): #if exists in tweets
			for line in lines: #read sorted from beginning
				joo=line.split()
				if (joo[1] == j) or ((joo[1]+"/")==j):
					mylist.append(int(joo[0]))
	a=sum(mylist)					
	dataset.write(m[1]+"\t"+m[0]+"\t"+m[2]+"\t"+str(a)+'\n')
dataset.close()
fp.close()
read_urls.close()