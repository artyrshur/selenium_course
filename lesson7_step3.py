from selenium import webdriver
import time
import os

try:
    link = "https://www.etagi.com/"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[1]/div/button[2]').click()
    #input.send_keys('Artyr')
    input1 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/input')
    input1.send_keys('1000000')
    input2 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/input')
    input2.send_keys('3000000')
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
