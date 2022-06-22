from selenium import webdriver
import time
from selenium.webdriver.common.by import By


try:
    link = "https://www.etagi.com/"
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[1]/div/div/button[3]/div').click()
    checbox11 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[1]/div[2]/button').click()
    checkbox12 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[1]/div[2]/div/div/button[1]').click()
    input1 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div/input')
    input1.send_keys('1000000')
    input2 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[2]/div/div[2]/div[2]/div/input')
    input2.send_keys('3000000')
    input3 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div/input')
    input3.send_keys('5')
    input4 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/div/input')
    input4.send_keys('15')
    browser.implicitly_wait(2)
    checkbox5 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[4]/div[2]/button').click()
    browser.implicitly_wait(2)
    checkbox6 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[1]/div[4]/div[2]/div/div/button[1]').click()
    browser.implicitly_wait(2)
    btn2 = browser.find_element_by_xpath('//*[@id="wARPj2Cdgv"]/div[2]/div/div[2]/div[3]/a').click()
    browser.implicitly_wait(2)
    search = browser.find_element_by_xpath('//*[@id="object-list"]/div/div').click()
    browser.implicitly_wait(3)
    button = browser.find_element_by_css_selector('#etagiTabs > div._9xwA7._2DZKJ > div > div > nav > ul > li:nth-child(4)')
    button.click()
    #browser.execute_script("window.scrollBy(0, 330);", button)
    #btn3 = browser.find_element_by_css_selector('#content > div > div > div > div._11n5y > div._1PJ8R > div > div.pXm1d > a > button').click()
    #input6.send_keys('9177777777')
    #btn3 = browser.find_element_by_xpath('//*[@id="enterKeyOrder"]/button/span').click()
finally:
    time.sleep(10)
    browser.quit()