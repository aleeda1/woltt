import unittest
from selenium import webdriver
from locators.locators import Locators
from page.frontpage import OpenWebsite

class Website(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://wolt.com/en")

    def test_openwebsite(self):
        # Create an instance of the OpenWebsite class
        website = OpenWebsite(self.driver)
        website.click_accept()
        website.click_login()
        website.click_google()
        #self.assertIn("Wolt", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
