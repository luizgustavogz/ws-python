from pathlib import Path
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ROOT_FOLDER = Path(__file__).parent
CHROMEDRIVER_EXE = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_services = Service(executable_path=str(CHROMEDRIVER_EXE))
chrome_browser = webdriver.Chrome(
    service=chrome_services,
    options=chrome_options,
)

# chrome_options.add_argument('--headless')

chrome_browser.get('https://www.google.com.br/')
time.sleep(30)
