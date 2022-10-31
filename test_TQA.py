import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class HelloWorld(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    __image_login = '//*[@id="root"]/div/div[2]/div[1]/div[2]'

    @classmethod
    def SetUp(cls):
        driver = cls.driver
        driver.implicitly_wait(10)

    def test1_hello_world(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        element = driver.find_element(By.XPATH, self.__image_login).is_displayed()
        self.assertTrue(element)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
