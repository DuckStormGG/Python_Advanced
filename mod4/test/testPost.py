import json
import unittest
from mod4.forPOST_test import app


class TestPost(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        self.url = "/registration"
        self.correct_values = {'email': 'teste@xample.com', 'phone': 9221112233, 'name': 'Pavel', 'address': 'EKB', 'index': 1892,
                'comment': 'asd'}
    def test_email_correct(self):
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 200)
    def test_email_incorrect(self):
        self.correct_values["email"] = "incorrect"
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 400)

    def test_phone_correct(self):
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 200)

    def test_phone_incorrect(self):
        self.correct_values['phone'] = 0
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 400)
    def test_name_correct(self):
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 200)

    def test_name_incorrect(self):
        self.correct_values['name'] = ''
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 400)
    def test_address_correct(self):
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 200)

    def test_address_incorrect(self):
        self.correct_values['address'] = ""
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 400)
    def test_index_correct(self):
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 200)

    def test_index_incorrect(self):
        sent =  {'email': 'teste@xample.com', 'phone': 9221112233, 'name': 'Pavel', 'address': 'EKB', 'index': "",
                'comment': 'asd'}
        self.assertTrue(self.client.post(self.url, data=sent).status_code == 400)
    def test_comment_correct(self):
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 200)

    def test_comment_incorrect(self):
        self.correct_values['comment'] = ''
        self.assertTrue(self.client.post(self.url, data=self.correct_values).status_code == 400)