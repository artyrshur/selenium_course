from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Artyr")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Shur")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Ufa")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("RUSSIA")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

