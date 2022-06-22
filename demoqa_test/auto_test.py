from selenium import webdriver
import time

try:
    link = "https://demoqa.com/"
    browser = webdriver.Chrome()
    browser.get(link)

    card = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]').click()

    button = browser.find_element_by_id('item-1').click()
    checkbox = browser.find_element_by_xpath('//*[@id="tree-node"]/ol/li/span/label/span[1]').click()

    button2 = browser.find_element_by_id('item-2').click()
    browser.implicitly_wait(3)

    radioButton = browser.find_element_by_css_selector("[for='impressiveRadio']").click()
    radioB2 = browser.find_element_by_css_selector("[for='yesRadio']").click()


finally:
    time.sleep(10)
    browser.quit()