
from bs4 import BeautifulSoup
from requests import get
import requests
from urllib.request import Request, urlopen
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup

url = 'https://www.nga.org/coronavirus/'
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#
webpage = urlopen(req)
page_soup = soup(webpage)
accordions = page_soup.findAll('div', class_ = 'wp-block-atomic-blocks-ab-accordion ab-block-accordion ab-font-size-18' )
# print(accordions)

# find_all('summary', attrs = {'class': 'ab-accordion-title'})

def accordion():

    i=0;
    for accordion in accordions:
        # print(accordion.summary.text)
        # print(i)
        i+=1
        if i == 49: #get oregon
            print(accordion.summary.text)
            # print(accordion.find('ul'))
            ul = accordion.ul
            li = ul.findAll('li')
            print(li)

            # for index in li[2:len(li)]:
            #     print(index.text)




accordion()

# title = page_soup.find("title")
# print(title)
# containers = page_soup.findAll("p","promo")
# for container in containers:
#     print(container)