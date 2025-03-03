from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

def get_driver():
    options = Options()
    options.headless = False  
    
    service = Service(r"C:\dselenium\geckodriver.exe")
    driver = webdriver.Firefox(service=service, options=options)
    
    driver.implicitly_wait(5)  
    
    return driver
