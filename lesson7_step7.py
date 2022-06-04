from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")
button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button.click()
message = browser.find_element_by_id("verify_message")
assert "succesful" in message.text
browser.quit()