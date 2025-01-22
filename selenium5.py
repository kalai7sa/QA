from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
search_bar=driver.find_element(By.ID,"small-searchterms")
search_bar.send_keys("Lenova")
search_bar.click()
