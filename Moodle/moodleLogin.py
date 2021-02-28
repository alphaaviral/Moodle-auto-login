from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")
numbers = []
try:
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
  
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    
    

    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )

    a = login.text

    for word in a.split():
        if word.isdigit():
            numbers.append(int(word))
    
    if "add" in a:
        ans = numbers[0] + numbers[1]
    elif "subtract" in a:
        ans = numbers[0] - numbers[1]
    elif "first" in a:
        ans = numbers[0]
    elif "second" in a:
        ans = numbers[1]
    
    un = input("Enter your kerberos ID: ")
    username.send_keys(un)

    pw = input("Enter your kerberos password: ")
    password.send_keys(pw)


    ansfield = driver.find_element_by_id("valuepkg3")
    ansfield.clear()
    ansfield.send_keys(ans)

    button = driver.find_element_by_id("loginbtn")
    button.click()

except:
    driver.quit()

