from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_xpath('//*[@id="num1"]')
    y_element = browser.find_element_by_xpath('//*[@id="num2"]')
    x = x_element.text
    x = int(x)
    y = y_element.text
    y = int(y)
    z = x + y
    z = str(z)

    def sum(x, y):
        return str(x + y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    #select.click()
    select.select_by_value(z)
    #select.click()
    browser.find_element_by_xpath('/html/body/div/form/button').click()

finally:
    time.sleep(10)
    browser.quit()