#!/usr/bin/env python

# harvest.py - given a csv file, output bunches o' plain text files

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame and distributed under a GNU Public License

# December 5, 2021 - after a jazz concert w/ Magdalena and going to Bar Louie 


# configure
CSV    = './pamphlets/metadata.csv'
OUTPUT = './pamphlets'

# require
from multiprocessing import Pool
from pathlib         import Path
from tempfile        import TemporaryFile
from tika            import parser
import pandas        as     pd
import requests
import sys

# given a url, save a plain text file
def harvest( url, file ) :

	# debug
	sys.stderr.write( "\t".join( [ url, file ] ) + '\n' )

	# create output filename, and check to see if it exists
	filename = Path( OUTPUT )
	filename = filename / file
	if not filename.exists() :
			
		# get the remote content; needs error checking
		pdf = requests.get( url ).content
	
		# extract the plain text and save it; assume tika server is already running
		text = parser.from_buffer( pdf )[ 'content' ]
		with open( filename, 'w' ) as handle : handle.write( text )

# main
if __name__ == '__main__' :

	# initialize
	pool     = Pool()
	records  = pd.read_csv( CSV )
	requests = []
	
	# process each record; create a list of requests
	for index, record in records.iterrows() :
	
		# parse and update
		url  = record[ 'url' ]
		file = record[ 'file' ]
		requests.append( [ url, file ] )
				
	# submit the work, clean up, and done
	pool.starmap( harvest, requests )
	pool.close()
	exit()

	
		
	
		


