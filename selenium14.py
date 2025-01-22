from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
print("printing all rows and columns data........")
number_of_rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
number_of_columns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
for r in range(2,number_of_rows+1):
    authorName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        BookName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(BookName,"    ",authorName,"     ",price)


        #select book name written by author Mukesh