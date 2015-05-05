from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_is_presented_with_username_login(self):
        # Tim goes to homepage and sees Longoria Guestbook title followed by
        # "Wordfib" sub title
        self.browser.get('http://localhost:8000')
        self.assertIn('Longoria Guestbook', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Wordfib', header_text)
    # the homepage however has the Wordfib game(balderdash clone).
    # The user is prompted to input last initial followed by first name
    # for scoring purposes.
    # There is a wordfib logo and user is presented with a word and
    # at LEAST three definitions (if necessary setup at databse init time)
    # but more definitions if they are available. User must attempt to 
    # select the true definition among (hopefully) user-submitted ones.
    # After guessing, if correct Tim gets points! If incorrect, whoever
    # wrote the false def gets points. After that, then the user is
    # prompted to write a def for a different randomly selected word.
    # AND THEN, leaderboard is shown.
    # Tim goes to homepage There is a menu with links to guestbook,
    # and "local stuff". Local stuff will have parks, movies, maybe 
    # API stuff from qctimes, rcreader, nearby restaurants, personalized
    # reccommendations for walks, runs, rides, hikes. etc.
    # Guestbook will have place to post a note, upload a picture.        
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')

