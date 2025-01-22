from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://automationexercise.com/api_list")
search_box=driver.find_element(By.ID,"search_product")
search_box.send_keys("Blue Top")
submit_button=driver.find_element(By.ID,'submit_search')
submit_button.click()
