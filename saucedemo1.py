from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
search_bar=driver.find_element(By.ID,"user-name")
search_bar.send_keys("standard_user")

search_bar=driver.find_element(By.ID,"password")
search_bar.send_keys("secret_sauce")

submit_button=driver.find_element(By.ID, "login-button")
submit_button.click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

add_to_cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
)
add_to_cart.click()

add_to_cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
)
add_to_cart.click()

add_to_cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "checkout"))
)
add_to_cart.click()
search_bar=driver.find_element(By.ID,"first-name")
search_bar.send_keys("Kal")

search_bar=driver.find_element(By.ID,"last-name")
search_bar.send_keys("Sel")

search_bar=driver.find_element(By.ID,"postal-code")
search_bar.send_keys("75068")
#driver.save_screenshot("D:/Python/testing_automation.png")

print(driver.title)
