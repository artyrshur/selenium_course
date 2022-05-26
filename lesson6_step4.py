from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000)))
    input.click()
    input1 = browser.find_element_by_xpath('/html/body/div/form/div[1]/input')
    input1.send_keys("Artyr")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[2]/input")
    input2.send_keys("Shurshin")
    input3 = browser.find_element_by_xpath('/html/body/div/form/div[3]/input')
    input3.send_keys("Ufa")
    input4 = browser.find_element_by_xpath('/html/body/div/form/div[4]/input')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('/html/body/div/form/button')
    button.click()

finally:

    time.sleep(30)

    browser.quit()
