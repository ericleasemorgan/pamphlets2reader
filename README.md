# Pamphlets2Reader

Given a set of MARC records, the two Python scripts in this repository will create a directory of content suitable for processing by the Distant Reader; this is a demonstration of how MARC data can be used as input to a thing called the [Distant Reader](https://distantreader.org).


## Cookbook

  1. `./bin/marc2csv.py 2>/dev/null > ./pamphlets/metadata.csv`
  2. `java -jar tika-server.jar`
  3. `./bin/harvest.py`
  4. `zip -r pamphlets.zip pamphlets/*`

Use the resulting `pamphlets.zip` file as input to the Reader at [https://distantreader.org/create/zip2carrel](https://distantreader.org/create/zip2carrel).


## Introduction

If you have MARC records, and if your MARC records include URLs in 856$u, and if those URLs point to content as opposed to splash pages, then you can use the scripts in this repository as a framework for creating data sets from those MARC records. By doing so, you will be enabling students, researchers, and scholars to do distant reading against the content of the URLs.

Here in the Hesburgh Libraries we have such a set of MARC records. More specifically, we have a set of records describing about 2,000 Catholic pamphlets. You know. Those free little booklets found in the back of many Catholic churches. The pamphlets have titles like "Shall I marry a non-Catholic?", "Give him a thought", or "A brief introduction to the divine office". Each MARC record includes a URL pointing to a PDF file, and each PDF file has been OCRed so the underlying text is embedded within.

This is perfect fodder for the Distant Reader. Given the OCRed data, the Reader will be able to do all sorts of feature extraction (ngrams, parts-of-speech, named entities, and grammars), list bibliographics (authors, titles, years, extents, statistically significant keyword, and summaries), and support concordancing, full text indexing, semantic indexing, and topic modeling. Given these features, one can address all sorts of interesting questions. Examples might include: to what degree were the pamphlets intended to be read by children or adults, what were some common themes in the pamphlets and how did those themes ebb &amp; flow over time, or how was the word "love" used throughout the collection?


## The scripts

There are only two scripts needed to do the work.

The first, [`marc2csv.py`](./bin/marc2csv.py) reads a given file of MARC records, extracts metadata (author, title, year, URL, and system number), and outputs the metadata as a CSV file suitable for consumption by the Reader. The script is straight-forward. It ought to work out-of-the-box, but your MARC records will most likely be somewhat different. Consequently, use `marc2csv.py` as a framework for your specific environment.

The second script, [`harvest.py`](./bin/harvest.py) is a bit trickier. It reads the CSV file from the previous step, creates a queue of things to download, and processes the queue in parallel. This means, it processes the queue with as any processors ("cores") you have in your computer, which can considerably speed up the harvesting process. As it downloads the remote content, it uses [Tika](https://tika.apache.org) to extract the OCR, and saves the result to the file system. (It is up to you to load the Tika server and run it as a separate process.)

Once you have gotten this far, compress (zip) the pamphlets directory and all it contains. You can then submit the compressed file to the Distant Reader. The Reader will then do the feature extraction, save the result as a data set, and one can analyze the data set in order to address the interesting questions. This data set ("study carrel") has already been created, and it is temporarily available to [read](http://dh.crc.nd.edu/tmp/catholic-pamphlets/index.htm), [browse](http://dh.crc.nd.edu/tmp/catholic-pamphlets/), or [download](http://dh.crc.nd.edu/tmp/catholic-pamphlets/study-carrel.zip). 


## Summary

Suppose you have digitized a number of collections, and suppose you have described them using MARC. If so, then you may be able to use the scripts in this repository to enhance access to those collections. Use the MARC records to create input for the Distant Reader. Save the output of the Distant Reader (a "study carrel") on the 'Net where anybody can get it, and thus allow students, researchers, and scholars to query the collection in new and enhanced ways -- distant reading. 

---
Eric Lease Morgan &lt;emorgan@nd.edu&gt;  
December 7, 2021
