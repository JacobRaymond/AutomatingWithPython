from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#Open browser and go to url
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

#Washington and US box
source=driver.find_element_by_xpath('//*[@id="box3"]')
dest=driver.find_element_by_xpath('//*[@id="box103"]')

#Drag and drop
actions=ActionChains(driver)
actions.drag_and_drop(source, dest).perform()