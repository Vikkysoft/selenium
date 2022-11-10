import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_element_fields(element):
    print("Text:", element.text)
    print("Size:", element.size)
    print("Tag name:", element.tag_name)
    print("Location:", element.location)
    print("Accessible Name:", element.accessible_name)
    print("ID:", element.id)
    print("Aria Role:", element.aria_role)
    print("Rectangle:", element.rect)


def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://testifyltd.com/contact")
    #element = driver.find_element(By.TAG_NAME, "h2")
    #print_element_fields(element)
    element = driver.find_element(By.LINK_TEXT, "Academy")
    print_element_fields(element)


if __name__ == '__main__':
    main()
