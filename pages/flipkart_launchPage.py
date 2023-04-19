import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class launchPage(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    #Locators
    Search_Item_Field="//input[@placeholder='Search for products, brands and more']"
    Click_Button="//button[@type='submit']"

    def search_item(self, searchItem):
        self.driver.find_element(By.XPATH, self.Search_Item_Field).send_keys(searchItem)

    def click_search(self):
        search_option = self.driver.find_element(By.XPATH, self.Click_Button)
        search_option.click()
        time.sleep(5)


    def search_Items(self, searchItem):
        self.search_item(searchItem)
        self.click_search()





