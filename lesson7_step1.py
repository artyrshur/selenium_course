#считаем функцию передаем значение этой функции в поле, скролим вниз на 150 пикс, отмечаем чек-бокс, радиобатон,
#и нажимаем сабмит
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(int(x))

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 150);", button)

    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()

    radioB = browser.find_element_by_css_selector("[for = 'robotsRule']")
    radioB.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(10)
    browser.quit()



