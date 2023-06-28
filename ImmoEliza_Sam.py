import requests
from bs4 import BeautifulSoup as soup
import re

# Get list of houses for sale
url = "https://www.immoweb.be/en/search/house/for-sale"
response = requests.get(url)
# Make a soup
overview_page = soup(response.text, 'html.parser')
# Initialize an empty list
houses_links = []
# Find individual links
for element in overview_page.find_all("a", attrs={"aria-label": re.compile("House for sale*?")}):
    houses_links.append(element.get('href'))

# Test with 1 house
#house_page = requests.get(houses_links[0]).text

#https://www.immoweb.be/en/classified/house/for-sale/libin/6890/10657263     
#    

url = "https://www.immoweb.be/en/classified/house/for-sale/libin/6890/10657263"
house_page = requests.get(url)
house_page = soup(house_page.text, 'html.parser')
rows = house_page.find_all("tr", attrs={"class": "classified-table__row"})
for row in rows:
    # Get keys to build dict
    header = row.find("th", attrs={"class": "classified-table__header"})
    header = re.sub("\<.*row\">", "", str(header))
    header = re.sub("\<\/th>", "", str(header))
    header = re.sub("( ){2,}", "", str(header))
    header = re.sub("\\n", "", str(header))

    # Get values
    data = row.find("td", attrs={"class": "classified-table__data"})
    data = re.sub("\<.*data\">", "", str(data))
    data = re.sub("\<\/td>", "", str(data))
    data = re.sub("( ){2,}", "", str(data))
    data = re.sub("\\n", "", str(data))
    data = re.sub("\<span.+span>", "", str(data))
    
    house_dict = {}
    #house_dict['locality'] = 
    
    classified_script = house_page.find("div", attrs={"id": "container-main-content"}).script.text
    dict = r"window.classified = \{.+\}"
    print(dict)
    if header == "Tenement building": 
        break
