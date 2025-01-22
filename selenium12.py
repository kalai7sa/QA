from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
number_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
number_of_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(number_of_rows)
print(number_of_columns)
driver.close()


#count no of rows and columns