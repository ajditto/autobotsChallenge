import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):

    def setUp(self):
        # startup webdriver
        self.driver = webdriver.Chrome('/Users/andrewditto/code/personal/pyChallenge/chromedriver')

    def tearDown(self):
        # close webdriver
        self.driver.close()

    def test_challenge1(self):
        # test steps
        self.driver.get('https://www.google.com')
        self.assertIn('Google', self.driver.title)


if __name__ == '__main__':
    unittest.main()
