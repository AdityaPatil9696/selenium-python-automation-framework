import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class searchResult(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver


    #Locators
    Filter_Result_Field="//div[@title='Women']//div[@class='_24_Dny']"


    def filter_result(self):
        watch_f_women = self.driver.find_element(By.XPATH, self.Filter_Result_Field)
        watch_f_women.click()
        time.sleep(5)







