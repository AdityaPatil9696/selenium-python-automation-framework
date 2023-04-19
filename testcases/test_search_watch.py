import time

import pytest
#from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.flipkart_launchPage import launchPage
from pages.search_resultPage import searchResult
#from ddt import ddt, data, file_data, unpack
#from openpyxl import Workbook, load_workbook


@pytest.mark.usefixtures('setup')
#@ddt
class TestSearchAndVerifyfilter():

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = launchPage(self.driver)

    #@data(("watch"))
    #@unpack
    #@file_data("../testdata/testdata.json")
    def test_search_watch(self):

        self.lp.search_Items("watch")

        sr=searchResult(self.driver)
        sr.filter_result()

        self.lp.page_scroll()

        #click on checkboxes for more options
        #clear_checkboxes=self.driver.find_element(By.XPATH,"//div[@class='HbxufK']//span[contains(text(),'Clear all')]")

        check_boxes=self.driver.find_elements(By.XPATH,"//body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/section[5]/div[2]/div[1]")
        i=1
        for i in (len(check_boxes) - 2, 7):
            if i < 2:
                check_boxes[i].click()
                time.sleep(5)

