# выполни подсчет выражения и вставь этот ответ выражения в строку, затем выполни алерт и нажми ок
#
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element
    y = calc(int(x))

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    time.sleep(10)
    browser.quit()
