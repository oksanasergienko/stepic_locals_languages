from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_button(browser):
    browser.get(link)
    time.sleep(20)

    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_to_basket_button, "Button 'Add to basket' is not found"

