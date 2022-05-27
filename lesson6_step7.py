from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys("Artyr")
    input1 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[2]/input")
    input1.send_keys("Shur")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[1]/div[3]/input")
    input2.send_keys("artyr@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

