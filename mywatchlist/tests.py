from django.test import TestCase

# Create your tests here.
class AppTest(TestCase):
    def test_show_html_exists(self):
        response = self.client.get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_show_xml_exists(self):
        response = self.client.get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_show_json_exists(self):
        response = self.client.get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
