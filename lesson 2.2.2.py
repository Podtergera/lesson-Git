from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log("a +b"))

    a_element = browser.find_element(By.ID, "num1")
    a = a_element.text
    b_element = browser.find_element(By.ID, "num2")
    b = b_element.text
    z = str(int(a) + int(b))

    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(str(z))
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

