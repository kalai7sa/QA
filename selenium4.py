from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
search_bar=driver.find_element(By.NAME,"username")
search_bar.send_keys("Admin")
search_bar=driver.find_element(By.NAME,"password'")
search_bar.send_keys("admin123")
login_button=driver.find_element(By.ID,"login_button")
login_button.click()
print(driver.title)


