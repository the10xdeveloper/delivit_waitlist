from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class TestPage(TestCase):
    def test_index_page_works(self):
        response = self.client.get(reverse('waitlist:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index_view.html')
        # self.assertContains(response, 'Welcome to the waitlist app')

    def test_waitlist_page_works(self):
        response = self.client.get(reverse('waitlist:join_waitlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'waitlist_view.html')
        # self.assertContains(response, 'Join the waitlist')
        pass

    pass
