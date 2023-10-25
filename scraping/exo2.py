import requests
from bs4 import BeautifulSoup

for page_num in range(1, 4):
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={page_num}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'class': 'table'})
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 0:
                equipe = cells[0].text.strip()
                annee = cells[1].text.strip()
                pourcentage = cells[5].text.strip()
                print(f'{equipe} - {annee} - {pourcentage} %')
    else:
        print(f'La requête pour la page {page_num} a échoué avec le code d\'état {response.status_code}')
