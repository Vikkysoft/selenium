import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def locate_by_class_name(driver):
    subscribe_for_updates = driver.find_element(By.CLASS_NAME, "react-reveal")
    print("Subscribe for updates", subscribe_for_updates)


def locate_by_xpath(driver):
    explore_by_full_xpath = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div/div[1]/div/button')
    print("Explore by full Xpath:", explore_by_full_xpath)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://academy.testifyltd.com/")
    locate_by_class_name(driver)
    locate_by_xpath(driver)


if __name__ == "__main__":
    main()
