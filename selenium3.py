from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://demoqa.com/text-box")
search_bar=driver.find_element(By.ID,"userName")
search_bar.send_keys("Kalai Selvi")

search_bar=driver.find_element(By.ID,"userEmail")
search_bar.send_keys("KalaiSelvi@example.com")

search_bar=driver.find_element(By.ID,"currentAddress")
search_bar.send_keys("1234 Temporary Dr")

search_bar=driver.find_element(By.ID,"permanentAddress")
search_bar.send_keys("5678 Non-Temporary Dr")

submit_button=driver.find_element(By.ID, "submit")
submit_button.click()

#driver.save_screenshot("D:/Python/testing_automation.png")

print(driver.title)
