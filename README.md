
# Dirbot

This is a demonstration Scrapy project to scrape entries from the [DMOZ Archive](http://dmoztools.net/). It compliments another scrapy demo [quotesbot](https://github.com/scrapy/quotesbot).

This project is only meant for educational purposes.

## Extracted data

This project extracts the URL, Title and Description of the entries on a few pages on [dmoztools.net](http://dmoztools.net/)

The extracted data looks like this sample:

	{
		"url": "http://www.diveintopython.net/", 
		"name": "Dive Into Python 3", 
		"description": "By Mark Pilgrim, Guide to Python 3  and its differences from Python 2. ..."
	}


## Spiders

This project contains a single `dmoz` spider that demonstrates how to use XPath queries and Regular Expressions to extract data from a response. 

You can learn more about the spiders by going through the
[Scrapy Tutorial](http://doc.scrapy.org/en/latest/intro/tutorial.html).


## Running the spiders

You can run a spider using the `scrapy crawl` command, such as:

    $ scrapy crawl dmoz

If you want to save the scraped data to a file, you can pass the `-o` option:
    
    $ scrapy crawl dmoz -o quotes.json
