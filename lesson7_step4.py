# выполни подсчет выражения и вставь этот ответ выражения в строку, затем выполни алерт и нажми ок

import math
import time

import pyperclip
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("/html/body/form/div/div/button")
    button.click()
    alert = browser.switch_to.alert  #нажимает на кнопку всплывающего окна ок
    alert.accept()
    time.sleep(1)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(int(x))
    time.sleep(1)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)

    input = browser.find_element_by_id("answer")
    time.sleep(0.1)
    input.send_keys(y)
    #time.sleep(1)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]#копирует текст алерта в буфер потом просто вставить и все
    pyperclip.copy(addToClipBoard)
    print(alert_text)#выводит в консоль пайчарма ответ алерта
    alert = browser.switch_to.alert
    alert.accept()#нажми ок в алерте
    browser.quit()
