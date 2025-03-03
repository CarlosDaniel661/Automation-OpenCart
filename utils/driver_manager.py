from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    
    service = Service(executable_path="/usr/local/bin/chromedriver")


    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver