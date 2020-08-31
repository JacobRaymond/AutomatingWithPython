from selenium import webdriver

#Open browser and go to url
driver = webdriver.Chrome()
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")

#Write message in message field (extract xpath from inspect)
messageField=driver.find_element_by_xpath('//*[@id="user-message"]')
messageField.send_keys("Hello World") #Message to be added

#Click on "Show button"
showMessageButton=driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()

#Two input fields example
addFielda=driver.find_element_by_xpath('//*[@id="sum1"]')
addFielda.send_keys(5)
addFieldb=driver.find_element_by_xpath('//*[@id="sum2"]')
addFieldb.send_keys(9)
showTotal=driver.find_element_by_xpath('//*[@id="gettotal"]/button')
showTotal.click()