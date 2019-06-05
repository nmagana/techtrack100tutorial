import bs4 as bs
import urllib.request
import csv

# Website showcasing Britain's Top 100 fasting-growing companies
try:
    source = urllib.request.urlopen('https://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/')
except urllib.request.URLError:
    print('Error parsing url')
    exit(0)

soup = bs.BeautifulSoup(source, 'lxml')

# Step 1: Inspect the Web Page
# Look at the elements you want to get (i.e. tables)
# This website has tables, so let's extract that

# Side Note:
# Side note: Another check that can be done is to check whether a HTTP GET request 
# is being made on the website which may already return the results as structured 
# response such as a JSON or XML format. You can check this from within the network 
# tab in the inspect tools, often in the XHR tab. Once a page is refreshed it will 
# display the requests as they are loaded and if the response contains a formatted structure, 
# it is often easier to make a request using a REST Client such as Insomnia to return the output.

table = soup.find('table')
# Get all rows from table
results = table.find_all('tr')
# Get only table headers
table_headers = results[0]
# Get rest of table rows besides header
table_info = results[1:]
# Create list of headers
header_info = [header.text for header in table_headers.find_all('th')]
# Include Webpage as a column header
header_info.insert(2, 'Webpage')
# Create list to hold all rows
table_data = [[column.text if i != 1 else column for i, column in enumerate(row.find_all('td'))] for row in table_info]

# Clean Data
for row in table_data:
    for i, column in enumerate(row):
        # Extract Company and Website 
        if i == 1:
            # Extract company name from span
            company_name = column.find('span', class_='company-name').text
            row[i] = company_name

            # Get link of website 
            url = column.find('a').get('href')
            try:
                source = urllib.request.urlopen(url)
            except urllib.request.URLError:
                print('Error parsing url')
                exit(0)
            
            soup = bs.BeautifulSoup(source, 'lxml')
            # get side table
            table_rows = soup.find('table')
            # get website
            website = table_rows.find_all('tr')[-1].find('a').get('href')

        else:
            # clean these columns
            if i in [4, 5]:
                row[i] = row[i].strip('%*')
    
    row.insert(2, website)

# Create CSV file
with open('techtracktutorial.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(header_info)
    writer.writerows(table_data)

writeFile.close()