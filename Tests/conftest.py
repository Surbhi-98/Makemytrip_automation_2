import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--driver_path", action="store", default="/home/cbnits/Documents/Makemytrip_Assignment/chromedriver"       
    )
    parser.addoption("--headless", action="store", default="headless", help="Is headless driver?")

@pytest.fixture(scope="class")
def driver_setup(request):
    BASE_URL = "https://www.makemytrip.com/"
    browser_name = request.config.getoption("browser_name")
    driver_path = request.config.getoption("driver_path")
    headless = request.config.getoption("--headless")
    chrome_options = webdriver.ChromeOptions()
    if headless == "true":
        # Set headless flag to true
        chrome_options.add_argument("headless")
    chrome_options.add_argument('--ignore-certificate-error')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36")
    # chrome_options.add_argument("--remote-debugging-port=9222")
    # chrome_options.add_argument("--disable-setuid-sandbox") 
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('headless')  #Only necessary for jenkins build
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.binary_location = 'Version 104.0.5112.79 (Official Build) (64-bit)'
    if browser_name == "chrome":
        service_obj = Service("/home/cbnits/Documents/Makemytrip_Assignment/chromedriver")
        # service_obj = Service(driver_path)
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        agent = driver.execute_script("return navigator.userAgent")
        # print(agent)
        # driver = webdriver.Chrome(service=service_obj)
    driver.get(BASE_URL)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()