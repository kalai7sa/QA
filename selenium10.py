#from selenium import webdriver
#from selenium.webdriver.common.by import By
#driver=webdriver.Chrome()
#driver.get("https://rahulshettyacademy.com/angularpractice/")
#checkbox=driver.find_element(By.XPATH,"//*[@id='exampleCheck1']")
#checkbox.click()
#print(checkbox.is_selected())
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
dropdown_elements=driver.find_element(By.XPATH,"//*[@id='exampleFormControlSelect1']")
gender_dropdown=Select(dropdown_elements)
gender_dropdown.select_by_visible_text('Male')
selected_option = gender_dropdown.first_selected_option
print(selected_option.text)
driver.quit()







