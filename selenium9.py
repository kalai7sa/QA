from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")
driver.back()
#driver.forward()
#driver.refresh()

#driver.quit()
