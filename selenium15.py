from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver. switch_to.frame(0)
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

month='February'
year='2026'
date='20'
while True:
  mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
  yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
  if mon==month and yr==year:
    break
  else:
    driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
  if ele.text==dates:
    ele.click()
    break
