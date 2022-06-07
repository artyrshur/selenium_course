# неявное ожидание пока цена на билет не станет = 100 долларов, нажми на кнопку бук когда цена = 100,
# выполни капчу - реши уравнение и нажми сабмит
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
    (By.ID, "price"), "$100"))  # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_id("book").click()
browser.execute_script("window.scrollBy(0, 330);", button)

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(int(x))


input = browser.find_element_by_id('answer')
input.send_keys(y)
btn = browser.find_element_by_id("solve")
time.sleep(1)
btn.click()
alert = browser.switch_to.alert#переключись на окно алерта
alert_text = alert.text
print(alert_text)#принтует текст алерта в консоль иде
browser.quit()
