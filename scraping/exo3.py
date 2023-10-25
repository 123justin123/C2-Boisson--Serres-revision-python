import requests
from bs4 import BeautifulSoup
import csv


def get_doctors_info(session, writer):
    for i in range(1, 21):
        url = f'http://annuairesante.ameli.fr/professionnels-de-sante/recherche/liste-resultats-page-{i}-par_page-20-tri-aleatoire.html'
        reponse = session.get(url)
        soup = BeautifulSoup(reponse.text, 'html.parser')
        item_professionnel = soup.find_all('div', {'class': 'item-professionnel'})
        for item in item_professionnel:
            classes = ['nom_pictos', 'item left adresse', 'item left tel']
            elements = [item.find('div', {'class': classe}) for classe in classes]
            noms = [e.text.strip() if e is not None else None for e in elements]
            nom, adresse, telephone = noms
            writer.writerow({'Nom': nom, 'Adresse': adresse, 'Téléphone': telephone})


def post_search(session):
    url = 'http://annuairesante.ameli.fr/recherche.html'
    data = {
        "type": "ps",
        "ps_nom": "",
        "ps_profession": "34",
        "ps_profession_label": "Médecin+généraliste",
        "ps_acte": "",
        "ps_acte_label": "",
        "ps_type_honoraire": "indifferent",
        "ps_carte_vitale": "2",
        "ps_sexe": "1",
        "es_nom": "",
        "es_specialite": "",
        "es_specialite_label": "",
        "es_actes_maladies": "",
        "es_actes_maladies_label": "",
        "es_type": "3",
        "ps_localisation": "HERAULT+(34)",
        "ps_proximite": "on",
        "localisation_category": "departements",
        "submit_final": "Rechercher"
    }
    reponse = session.post(url, data=data)
    if reponse.status_code == 200:
        get_doctors_info(session, writer)

    success = reponse.status_code == 200
    return success


with open('result.csv', 'w', newline='') as csv_file:
    fieldnames = ['Nom', 'Adresse', 'Téléphone']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    session = requests.Session()
    if post_search(session):
        get_doctors_info(session, writer)
