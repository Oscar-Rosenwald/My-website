from selenium import webdriver
import unittest

class FunctionalTests(unittest.TestCase):
    def setUp(self):
       self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_if_it_works(self):
       self.fail('Failing on purpose!') 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
