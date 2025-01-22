#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#=webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()
search_bar=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
search_bar.is_displayed()
print("Display status:",search_bar.is_displayed())
print("Enable status:",search_bar.is_enabled())



