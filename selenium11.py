from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
alertwindow=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
alertwindow.click()
alertwindow=driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
alertwindow.accept()
#alertwindow.dismiss()
result_text=driver.find_element(By.XPATH,"//p[@id='result']")   
print(result_text.text)
