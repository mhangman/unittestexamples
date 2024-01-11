from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#install webdriver
service = Service(ChromeDriverManager().install())

#create web driver instance
driver = webdriver.Chrome(service=service)

#get page
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(2)

#get title
title = driver.title
time.sleep(2)
print(title)

#textbox bul, submit button bul locatorlarla
text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#textbox icine selenium yaz ve clickle
text_box.send_keys("Selenium")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text
print(text)

#quit browser
driver.quit()