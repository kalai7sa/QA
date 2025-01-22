from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://automationexercise.com/products")
driver.maximize_window()
search_bar=driver.find_element(By.XPATH,"/html/body/section/div/div[2]/div[1]/div[1]/h2")
search_bar.click()
                               