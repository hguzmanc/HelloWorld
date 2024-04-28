import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner


class HelloWorld(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    __image_login = '//*[@id="root"]/div/div[1]'
    __user_name = '//*[@id="user-name"]'
    __user_password = '//*[@id="password"]'
    __button_login = 'login-button'
    __tittle_home = '//*[@id="header_container"]/div[1]/div[2]/div'
    __container_error = '//*[@id="login_button_container"]/div/form/div[3]'
    __text_error = "Epic sadface: Username and password do not match any user in this service"

    @classmethod
    def SetUp(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(3)

    def test1_hello_world(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        element = driver.find_element(By.XPATH, self.__image_login).is_displayed()
        self.assertTrue(element)
        driver.find_element(By.XPATH, self.__user_name).send_keys("standard_user_test")
        driver.find_element(By.XPATH, self.__user_password).send_keys("secret_sauce")
        driver.find_element(By.ID, self.__button_login).click()
        element_error = driver.find_element(By.XPATH, self.__container_error).is_displayed()
        self.assertTrue(element_error)
        text_error = driver.find_element(By.XPATH, self.__container_error).text
        self.assertEqual(text_error, "Epic sadface: Username and password do not match any user in this service")

    def test2_hello_world(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        element = driver.find_element(By.XPATH, self.__image_login).is_displayed()
        self.assertTrue(element)
        driver.find_element(By.XPATH, self.__user_name).send_keys("standard_user")
        driver.find_element(By.XPATH, self.__user_password).send_keys("secret_sauce")
        driver.find_element(By.ID, self.__button_login).click()
        time.sleep(5)
        element_home = driver.find_element(By.XPATH, self.__tittle_home).is_displayed()
        self.assertTrue(element_home)

    @classmethod
    def tearDown(cls):
        pass
       # cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports', report_name='HelloWorld'))
