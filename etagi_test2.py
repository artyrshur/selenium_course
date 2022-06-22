from selenium import webdriver
import time


try:
    link = "https://www.etagi.com/"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.implicitly_wait(3)
    button = browser.find_element_by_css_selector('#mOz5TEp5HP > div > div > div > a:nth-child(3)').click()
    button2 = browser.find_element_by_css_selector('#mOz5TEp5HP > div > div > div > a:nth-child(2)').click()
    button3 = browser.find_element_by_css_selector('#hqj9FBMor0 > div.arow > div > div:nth-child(2) > div.col-3 > a > span')
    button3.click()
    input = browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/input[2]').click()
    input1 = browser.find_element_by_xpath('//*[@id="content"]/div[3]/div/div[2]/div[2]/div[2]/div[4]/div/div/div/input[2]')
    input1.send_keys('9177777777')


finally:
    time.sleep(5)
    browser.quit()