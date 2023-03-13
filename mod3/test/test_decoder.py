import unittest
from mod3.decoder import decrypt


class TestDecoder(unittest.TestCase):
    def test_one_dot(self):
        self.assertTrue(decrypt("абра-кадабра.") == "абра-кадабра")
    def test_two_dots(self):
        self.assertTrue(decrypt("абраа..-кадабра") == "абра-кадабра")
    def test_three_dots(self):
        self.assertTrue(decrypt("абраа..-.кадабра") == "абра-кадабра")
    def test_two_dots_before_dash(self):
        self.assertTrue(decrypt("абра--..кадабра") == "абра-кадабра")
    def test_three_dots_before_one_char(self):
        self.assertTrue(decrypt("абрау...-кадабра") == "абра-кадабра")
    def test_double_dots_equal_char_in_word(self):
        self.assertTrue(decrypt("абра........") == "")
    def test_one_char_left(self):
        self.assertTrue(decrypt("абр......a.") == "a")
    def test_three_dots_with_numbers(self):
        self.assertTrue(decrypt("1..2.3") == "23")
    def test_only_one_dot(self):
        self.assertTrue(decrypt(".") == "")
    def test_dots_more_than_char(self):
        self.assertTrue(decrypt("1.......................") == "")



