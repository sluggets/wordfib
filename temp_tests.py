from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_can_catch_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Longoria Guestbook', self.browser.title)
 
if __name__ == '__main__':
    unittest.main(warnings='ignore')
