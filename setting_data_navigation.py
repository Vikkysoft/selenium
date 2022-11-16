import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://testifyltd.com/contact")
    time.sleep(2)
    driver.refresh()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "About us").click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    time.sleep(5)


if __name__ == '__main__':
    main()

