# filtersum_urls
Filters a file containing counted urls (file3) with a record list (file4), counts the total number of occurrences of every 
record in the file with urls and stores them in 'output.csv' (file4 with an extra column for the counts).

command:	filtersum.py file1 file2 file3 file4

file4: tab separated record list containing record data (3 fields) and all correspodnig urls for each record (record 	url1	url2	..	urln)
file1: line separated url list extracted from each record and aggregated into a file
file3: line separated url list with counts from web corpus (count url)
file2: line separated url list from web corpus without counts
