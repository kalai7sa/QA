from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
print("printing all rows and columns data........")
number_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
number_of_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
for r in range(2,number_of_rows+1):
  for c in range(1,number_of_columns+1):
    data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
    print(data,end='     ')
    print()
