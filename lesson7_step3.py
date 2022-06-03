from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_xpath('/html/body/div/form/div/input[1]')
    input.send_keys('Artyr')
    input1 = browser.find_element_by_xpath('/html/body/div/form/div/input[2]')
    input1.send_keys('Shur')
    input2 = browser.find_element_by_xpath('/html/body/div/form/div/input[3]')
    input2.send_keys('arty@gmail.com')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = 'file.txt'
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_xpath('//*[@id="file"]')
    element.send_keys(file_path)
    input3 = browser.find_element_by_xpath('/html/body/div/form/button')
    input3.click()

finally:
    time.sleep(1)
    browser.quit()
