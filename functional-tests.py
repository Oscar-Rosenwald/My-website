from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time

class FunctionalTests(unittest.TestCase):
    def setUp(self):
       self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_if_it_works(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Website', self.browser.title)

        buttons = self.browser.find_elements_by_tag_name('button')
        self.assertEqual(len(buttons), 2)

        # TODO Check, if by clicking on the buttens we are taken to the correct
        # webpage

        # Blogs
        button = self.browser.find_element_by_id('button-posts')
        button.click()
        time.sleep(1)
        self.assertIn('Blogs', self.browser.find_element_by_tag_name('h2').text)

        posts = self.browser.find_elements_by_tag_name('a')
        self.assertTrue(len(posts) > 0)
        posts[1].click()
        time.sleep(1)
        self.assertEqual(len(self.browser.find_elements_by_tag_name('h3')), 1)

        # Check a back button to blog
        button = self.browser.find_element_by_tag_name('button')
        button.click()
        time.sleep(1)
        self.assertIn('Blogs', self.browser.find_element_by_tag_name('h2').text)
        
        # Check for the home button
        button = self.browser.find_element_by_tag_name('a')
        button.click()
        time.sleep(1)
        self.assertIn('My School', self.browser.find_element_by_tag_name('h2').text)

        # CV
        button = self.browser.find_element_by_id('button-CV')
        button.click()
        time.sleep(1)
        self.assertIn('My CV', self.browser.find_element_by_tag_name('h2').text)

        self.fail('Failing on purpose!') 


if __name__ == '__main__':
    unittest.main(warnings='ignore')
