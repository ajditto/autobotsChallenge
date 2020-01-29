import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/andrewditto/code/personal/pyChallenge/chromedriver')
        self.driver.set_page_load_timeout(30)

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get('https://www.copart.com')
        search = self.driver.find_element_by_id('input-search')
        search.send_keys('exotics')
        search.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'tableForm')))
        results = self.driver.find_element_by_name('tableForm')
        assert 'PORSCHE' in results.text
