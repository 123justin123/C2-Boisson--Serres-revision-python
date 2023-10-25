import requests
from bs4 import BeautifulSoup
import csv

with open('result.csv', 'w', newline='') as csv_file:
    fieldnames = ['Equipe', 'Victoire', 'Défaite']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for page_num in range(1, 11):
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
                    victoire = cells[2].text.strip()
                    defaite = cells[3].text.strip()
                    diff = int(victoire) - int(defaite)
                    if diff > 0:
                        writer.writerow({'Equipe': equipe, 'Victoire': victoire, 'Défaite': defaite})
        else:
            print(f'La requête pour la page {page_num} a échoué avec le code d\'état {response.status_code}')
