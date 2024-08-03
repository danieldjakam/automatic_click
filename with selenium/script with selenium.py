from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def click_link_using_selenium(url, link_text):
    # Configuration de Selenium
    options = Options()
    options.add_argument('--headless')  # Exécuter Chrome en mode headless (sans interface graphique)
    options.add_argument('--disable-gpu')  # Nécessaire pour le mode headless sous Windows
    options.add_argument('--no-sandbox')  # Nécessaire pour le mode headless sous Linux

    # Initialiser le WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Ouvrir la page web
        driver.get(url)

        # Rechercher un lien par son texte
        try:
            # Rechercher le lien spécifié par son texte
            link = driver.find_element(By.XPATH, f"//a[contains(text(), '{link_text}')]")
            link.click()
            print(f"Lien '{link_text}' cliqué avec succès.")
        except NoSuchElementException:
            print(f"Erreur : Le lien '{link_text}' n'a pas été trouvé sur la page.")
        except WebDriverException as e:
            print(f"Erreur WebDriver lors du clic : {e}")

    except WebDriverException as e:
        print(f"Erreur lors de l'ouverture de la page : {e}")

    finally:
        # Fermer le navigateur
        driver.quit()

# Utiliser la fonction pour accéder et cliquer sur un lien
click_link_using_selenium('https://secretstoryafrique.com', 'NIKA')
