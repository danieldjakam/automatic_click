import requests
from bs4 import BeautifulSoup

url = "https://secretstoryafrique.com/"

def fetch_and_click_links(url):
    try:
        # Envoyer une requête GET pour récupérer le contenu de la page
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception HTTPError pour les codes de statut 4xx/5xx

        # Analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver tous les liens dans la page
        links = soup.find_all('a')
        print(links)
        # Parcourir les liens et effectuer une requête GET pour chaque lien
        for link in links:
            href = link.get('href')
            print(href)
            if href and href.startswith('http'):
                try:
                    print(f"Accéder au lien : {href}")
                    link_response = requests.get(href)
                    link_response.raise_for_status()  # Vérifier que la requête a réussi
                    # Traiter la réponse du lien ici si nécessaire
                except requests.exceptions.HTTPError as e:
                    print(f"Erreur HTTP en accédant à {href}: {e}")
                except requests.exceptions.RequestException as e:
                    print(f"Erreur de requête en accédant à {href}: {e}")

    except requests.exceptions.HTTPError as e:
        print(f"Erreur HTTP lors de l'accès à la page : {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erreur de requête lors de l'accès à la page : {e}")

# Utiliser la fonction pour accéder à une page
fetch_and_click_links(url)
