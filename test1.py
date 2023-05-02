from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com')
alpha = driver.find_element(By.NAME,"q")
alpha.send_keys("Selenium")
alpha.send_keys(Keys.ENTER)
time.sleep(10)
driver.find_element(By.XPATH, '//*[@class="LC20lb MBeuO DKV0Md"]').click()