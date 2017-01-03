from django.test import TestCase
from django.core.urlresolvers import reverse


class TestIndex(TestCase):
    def test_200(self):
        response = self.client.get(reverse('ui:index'))
        self.assertEqual(response.status_code, 200)