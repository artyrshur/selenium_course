#запускает браузер один раз и в нем выполняет тест один и два и после закрывается yield помогает выполнять без прерываний
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"#7


@pytest.fixture(scope="class")#выполни для всего класса без прерываний#1
def browser():#3
    print("\nstart browser for test..")#4
    browser = webdriver.Chrome()#5
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):#2
        print("start test1")#6
        browser.get(link)#7
        browser.find_element(By.CSS_SELECTOR, "#login_link")#8
        print("finish test1")#9

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")#10
        browser.get(link)#11
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")#12
        print("finish test2")#13