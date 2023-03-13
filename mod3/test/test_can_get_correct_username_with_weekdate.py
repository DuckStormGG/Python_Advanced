import unittest
import datetime

from mod3.greetings import app
from freezegun import freeze_time


class TestGreetings(unittest.TestCase):

    def setUp(self) -> None:
        app.config['Testing'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.base_url = '/hello-world/'
    def test_can_get_correct_username_with_weekdate(self):

        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        self.assertTrue(username in response_text)

    @freeze_time('2023-03-6')
    def test_can_get_correct_weekdate_monday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        weekday = 'Понедельника'
        self.assertTrue(weekday in response_text.split('.')[1])

    @freeze_time('2023-03-7')
    def test_can_get_correct_weekdate_tuesday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        weekday = 'Вторника'
        self.assertTrue(weekday in response_text.split('.')[1])

    @freeze_time('2023-03-8')
    def test_can_get_correct_weekdate_wednesday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        weekday = 'Среды'
        self.assertTrue(weekday in response_text.split('.')[1])

    @freeze_time('2023-03-9')
    def test_can_get_correct_weekdate_thursday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        weekday = 'Четверга'
        self.assertTrue(weekday in response_text.split('.')[1])

    @freeze_time('2023-03-10')
    def test_can_get_correct_weekdate_friday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        weekday = 'Пятницы'
        self.assertTrue(weekday in response_text.split('.')[1])

    @freeze_time('2023-03-11')
    def test_can_get_correct_weekdate_saturday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        weekday = 'Субботы'
        self.assertTrue(weekday in response_text.split('.')[1])

    @freeze_time('2023-03-12')
    def test_can_get_correct_weekdate_sunday(self):
        username = 'username'
        response = self.app.get(self.base_url + username)
        response_text = response.data.decode()
        weekday = 'Воскресенья'
        self.assertTrue(weekday in response_text.split('.')[1])
