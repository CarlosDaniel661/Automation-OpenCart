from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def get_driver():
    options = Options()
    options.headless = True
    #Geckodriver para entorno de linux
    service = Service(executable_path="/usr/local/bin/geckodriver")

    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    return driver