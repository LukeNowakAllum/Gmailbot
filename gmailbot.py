import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#Arrays to make it more efficient 
ButtonID=['//*[@id="L2AGLb"]/div','//*[@id="gb"]/div/div[1]/div/div[1]/a','//*[@id="identifierNext"]/div/button/span','//*[@id="passwordNext"]/div/button/span']
InputbarID =['//*[@id="identifierId"]','//*[@id="password"]/div[1]/div/div[1]/input']
TextInput=["botcosmicpigee@gmail.com","Testpassword1234"]

#to keep the window open permanatly

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#location of the Chrome driver needed to interact with elements and open browser 
driver = webdriver.Chrome(options=options,executable_path='./chromedriver_win32\chromedriver.exe')
driver.get("https://www.google.co.uk//")

# accepting terms and conditions and gmail button on chrome 
Button =driver.find_element(By.XPATH, ButtonID[0]).click()
Button =driver.find_element(By.XPATH, ButtonID[1]).click()

#input bar element interacted with and email username inputted 
InputBar =driver.find_element(By.XPATH,InputbarID[0])
InputBar.send_keys(TextInput[0])

#next button
Button =driver.find_element(By.XPATH, ButtonID[2]).click()

#Waits for the button to appear or until timeout  and inputs password
Password = WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.XPATH,InputbarID[1])))
time.sleep(1)
Password.send_keys(TextInput[1])

#next button
Button =driver.find_element(By.XPATH, ButtonID[3]).click()

print("Sucessfully Logged In ")


