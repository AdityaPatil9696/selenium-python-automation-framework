import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.flipkart.com/")
    ele = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    ele.click()
    request.cls.driver=driver
    yield
    driver.close()
