import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    country_divs = soup.find_all('div', {'class': 'country'})
    for country_div in country_divs:
        country = country_div.find('h3').text.strip()
        print(f'{country}')
