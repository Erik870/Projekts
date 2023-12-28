
import pandas 
import openpyxl
from openpyxl.styles import Font, Alignment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Inicializēt WebDriver
service = Service()
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

words=[]            # angļu valodas vārdi 
Translations = []   # latviešu valodas vārdi
Translations_2 = [] # krievu valodas vārdi

fails = pandas.read_excel("Words.xlsx", sheet_name="Sheet1")
info_list = fails.values.tolist()

for row in info_list:           #paņēm vārdus no "Sheet1" un ievadā masīvā: "words[]"
    words.append(row[0])

words.sort() # sakārto pēc alfabētas secība