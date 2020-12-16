import requests
url = 'https://sfbay.craigslist.org/search/cto?srchType=T&hasPic=1&min_price=100&min_auto_year=200&auto_drivetrain=1&auto_paint=1'
my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",  "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}

session = requests.Session()

page = session.get(url, headers=my_headers)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')
# soup = soup.prettify()
# print(soup.prettify())
soup.find_all('p')
elan_list = soup.find('div',id='sortable-results').find('ul',class_='rows').find_all('li')
for_i = 0
for elan_list_item in elan_list:
    detail_url = elan_list_item.find_all('a')
    detail_page = session.get(detail_url[0]['href'], headers=my_headers)
    detail_soup = BeautifulSoup(detail_page.text, 'html.parser')
    print(detail_url[0])
    print(detail_url[0]['href'])
    print(detail_soup.find('section',id='postingbody    '))
    # print(detail_url[0]['href'])
    # print(detail_soup.find('div',id='postingbody'))

    for_i += 1
    # print(elan_list_item)
soup.find_all(id='third')
soup.find_all('p', class_='chorus')