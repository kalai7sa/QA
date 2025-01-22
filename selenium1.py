from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver= webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
search_bar=driver.find_element(By.ID,"performance_glitch_user")
search_bar.send_keys("secret_sauce")
submit_button=driver.find_element(By.ID,"submit")
submit_button.click()
print(driver.title)