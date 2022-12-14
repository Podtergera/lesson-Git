from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    footer = browser.find_element(By.CLASS_NAME, "bd-footer.bg-light.text-muted")
    browser.execute_script('arguments[0].style.visibility = \'hidden\'', footer)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()
    button = browser.find_element(By.ID, "robotsRule")
    button.click()

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()
