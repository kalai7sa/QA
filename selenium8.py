from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
rd_male=driver.find_element(By.XPATH,"//*[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//*[@id='gender-female']")
print(rd_male.is_selected())
print(rd_female.is_selected())
rd_male.click()
print(rd_male.is_selected())
print(rd_female.is_selected())

