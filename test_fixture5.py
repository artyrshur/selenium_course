#автоиспользование фикстур параметр autouse=True, который укажет, что фикстуру нужно запустить для каждого
# теста даже без явного вызова, , браузер откроется два раза
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"# 4      11


@pytest.fixture()
def browser():
    print("\nstart browser for test..")# 2    8
    browser = webdriver.Chrome()# 3   9
    yield browser
    print("\nquit browser..")# 6    13
    browser.quit() # 14

@pytest.fixture(autouse=True)
def prepare_data():
    print()
    print("preparing some critical data for every test")# 1   7

class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)# 4
        browser.find_element(By.CSS_SELECTOR, "#login_link")# 5

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):# 2   8
        browser.get(link)# 10
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")# 12

