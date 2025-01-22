from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
act=ActionChains(driver)
washington_ele=driver.find_element(By.ID,"box3")
United_States_ele=driver.find_element(By.ID,"box103")
act.drag_and_drop(washington_ele,United_States_ele).perform()