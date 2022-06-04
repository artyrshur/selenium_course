import math
import time

import pyperclip
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath('/html/body/form/div/div/button')
    button.click()
    new_window = browser.window_handles[1]  # создаем вторую вкладку, теперь знаем что в браузере открыто две вкладки
    browser.switch_to.window(new_window) #переход на новую вкладку в этом сеансе
    first_window = browser.window_handles[0] #запоминает имя первой вкладки чтобы потом можно было вернуться
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(int(x))
    time.sleep(1)

    input = browser.find_element_by_id('answer')
    time.sleep(1)
    input.send_keys(y)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()

finally:
    time.sleep(0)
    print(browser.switch_to.alert.text)
    confirm = browser.switch_to.alert #нажимает ок в алерте - в всплывающем окне подтверждения
    confirm.accept() # тоже
    browser.quit()