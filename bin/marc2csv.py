#!/usr/bin/env python

# marc2csv.py - given a set of MARC records, output rudimentary CSV suitable for the Reader
# usage: ./bin/marc2csv.py 2>/dev/null > ./pamphlets/metadata.csv

# Eric Lease Morgan <emorgan@nd.edU>
# (c) University of Notre Dame; distributed under a GNU Public License

# December 5, 2021 - in the Culver Coffee Shop


# configure
MARC    = './etc/pamphlets.mrc'
TXT     = '.txt'
COLUMNS = [ 'author', 'title', 'date', 'file', 'url' ]
PREFIX  = '_'

# require
from pymarc   import MARCReader
import pandas as     pd
import string

# initialize
records = []

# process the given file
with open( MARC, 'rb' ) as handle :

	# process each record
	for record in MARCReader( handle ) :

		# parse out system number; there is only one
		identifier = record.get_fields( '001' )[ 0 ].data
		
		# create a file name; prepend an underbar to make it a string
		file = PREFIX + identifier + TXT
		
		# author; sometimes it doesn't exist
		if record.author() : author = record.author()
		else : author = ''
		
		# title, and normalize it
		title = record.title()
		title = title.replace( ' /', '' )
		
		# date; sometimes it doesn't exist
		if record.pubyear() : date = record.pubyear()
		else                : date = ''

		# munge the date into a year, and pass on bogus years
		date = str( date.translate( str.maketrans( "", "", string.punctuation ) ) )
		if len( date ) != 4 : continue
			
		# url; in this case, it is always the first one
		url = record.get_fields( '856' )[ 0 ].get_subfields( 'u' )[ 0 ]
		
		# update the list of records
		records.append( [ author, title, date, file, url ] )
		
# put the records into a dataframe, output as CSV, and done
records = pd.DataFrame( data=records, columns=COLUMNS ) 
print( records.to_csv( index=False ) )
exit()

