#неявные ожидания implicitly wait(better) вместо time.sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.implicitly_wait(5) #говорим искать веб элемент в течение 5 с так как кнопка не сразу появл на странице
browser.get('http://suninjuly.github.io/wait1.html')
button = browser.find_element(By.ID, "verify").click()
message = browser.find_element_by_id('verify_message')
assert "successful" in message.text

browser.quit()