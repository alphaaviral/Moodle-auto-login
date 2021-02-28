from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

contestNo =str(input("Input the contest number: "))
url = "https://codeforces.com/problemset/problem/" + contestNo +"/A"
driver = webdriver.Chrome(PATH)



driver.get(url)
