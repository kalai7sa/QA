from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://automationexercise.com/products")
# search_bar=driver.find_element(By.ID,"1")
# search_bar.send_keys("btn btn-default add-to-cart")
search_bar=driver.find_element(By.NAME,"Blue Top")
search_bar.click()
print(driver.title)