#Tells the script to wait before performing an action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Open browser and go to url
driver = webdriver.Chrome()
driver.get("https://www.google.com/earth/")

#Will throw an exception after 10 seconds if condition is not met (in this case, the "Lauch Earth" button becomes available
#If 10 seconds have passed and the wait button is still not available, command will not execute
wait=WebDriverWait(driver, 10)
launchEarthButtom=wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButtom.click()