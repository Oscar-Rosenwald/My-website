from seleniumlogin import force_login
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time

class FunctionalTests(unittest.TestCase):
    def setUp(self):
       self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_CV(self):

        # Check for home button
        self.browser.get('http://localhost:8000/cv/')
        self.assertIn('My CV', self.browser.find_element_by_tag_name('h2').text)
        home = self.browser.find_element_by_tag_name('a')
        home.click()
        time.sleep(1)
        self.assertIn('My Website', self.browser.find_element_by_tag_name('h1').text)
        buttons = self.browser.find_elements_by_tag_name('button')
        self.assertEqual(len(buttons), 2)

        # Go back to the CV page
        button = self.browser.find_element_by_id('button-CV')
        button.click()
        time.sleep(1)
        self.assertIn('My CV', self.browser.find_element_by_tag_name('h2').text)

        # Does the page include the necessary Personal Details?
        personal_details = self.browser.find_elements_by_class_name('personal')
        self.assertTrue(len(personal_details) >= 4)

        # DON'T KNOW HOW TO TEST, IF SOMETHING IS PRESENT, WHEN THAT THING MAY
        # OR MAY NOT BE DEPENDING ON THE EXISTANCE OF AN ENTRY IN THE DATABASE

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

if __name__ == '__main__':
    unittest.main(warnings='ignore')
