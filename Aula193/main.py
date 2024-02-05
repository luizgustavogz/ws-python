# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options: https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium: https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raíz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH)
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Exemplo
    # options = '--headless', '--disable-gpu'
    options = ()
    browser = make_chrome_browser(*options)

    # Abre o Google
    browser.get('https://www.google.com')

    # Espere para encontrar o elemento
    search_box = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, 'APjFqb')
        )
    )
    search_box.send_keys('Hello World!')
    search_box.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # Espera 10 segundos
    sleep(TIME_TO_WAIT)
