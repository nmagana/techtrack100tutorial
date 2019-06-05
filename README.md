# techtrack100tutorial

Followed [online](https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed) from Kerry Park as an intro to web-scraping.

## Overview

Using BeautifulSoup and UrlLib, the [Tech Track 100](https://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/) website was set into an LXML format to be parsed. 

The first step in web-scraping is to inspect the webpage to get a sense of the HTML elements and identify points of entry to parse. The main table was a good element to use. Parsing was then done to transform the table into a list of each row of the table. Each company in each row had a hyperlink that routed to another page with more information represented in table. This table had the website of the respective company. Using similar techniques, the website was extracted from this page and inserted into the list. 

The csv file can be found in this repo. 