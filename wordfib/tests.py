from django.test import TestCase

from django.core.urlresolvers import resolve

from wordfib.views import home_page
from wordfib.models import *

from django.http import HttpRequest

from django.template.loader import render_to_string

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        for i in range(1, 6):
            test_word = WordAndTrue.objects.create(word=('testword%s' % (i)), definition=('test real def %s' % (i)))
            test_word.save()
            for j in range(1, 5):
                fake_def = test_word.fakedefinitions_set.create(author='lzach', definition=('fake def %s for testword%s' % (j, i)))
                fake_def.save()
        

        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Longoria Guestbook</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))
        #expected_html = render_to_string('home.html')
        #self.assertEqual(response.content.decode(), expected_html) 

    
