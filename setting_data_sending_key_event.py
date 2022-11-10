import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def send_keys_to_element(element, *keys):
    element.send_keys(keys)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testifyltd.com/contact")
    send_keys_to_element(driver.find_element(By.NAME, "firstname"), "Agunbiade")
    send_keys_to_element(driver.find_element(By.NAME, "lastname"), "Victoria Bolupe")
    send_keys_to_element(driver.find_element(By.NAME, "email"), "bolvic28@gmail.com")
    send_keys_to_element(driver.find_element(By.NAME, "phone"), Keys.CONTROL, "V")
    time.sleep(10)


if __name__ == '__main__':
    main()