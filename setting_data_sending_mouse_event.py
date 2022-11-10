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
    send_keys_to_element(driver.find_element(By.NAME, "message"), "I'm just practising our Selenium/python automation class")

    form = driver.find_element(By.TAG_NAME, "form")
    #submit_button = form.find_element(By.TAG_NAME, "button")
    #submit_button.click()
    form.find_element(By.XPATH, '//*[@id="__next"]/main/section[1]/div/div[1]/div[2]/form/div[5]/button').click()
    form.find_element(By.TAG_NAME, "button").click()
    time.sleep(5)



if __name__ == '__main__':
    main()
