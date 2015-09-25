import csv
import sys
try:
	input_filename = sys.argv[1]
	output_filename = sys.argv[2]
	missing_data = sys.argv[3]
except IndexError:
	print "Usage: FilterColPHYLOViZ.py <input_file> <output_file> <missing_data>"
	print "Removes the columns of input_file containing missing_data and writes to output_file"
	print "jcarrico@fm.ul.pt  2/09/2013"
	raise SystemExit


f =open(input_filename, 'rb')
rdr = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)

result= open(output_filename,"wb")
wtr= csv.writer( result, delimiter='\t' )
cols2del=[];
for r in rdr:
	cols2del=cols2del+[i for i, x in enumerate(r) if x==missing_data]
print ' Original file contains ' + str(len(r)) +' columns.'
cols2del = sorted(set(cols2del), reverse=True)
f.seek(0)
for r in rdr:
	for i in cols2del:
		del r[i]
	wtr.writerow( r )

print 'Deleted ' + str(len(cols2del)) + ' columns.' + str(len(r)) + ' columns left in file' 
