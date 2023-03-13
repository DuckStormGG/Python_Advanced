import unittest
from mod3.person import Person

class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.name = "Pavel"
        self.yob = 2003
        self.address = "Ekaterinburg"
        self.person = Person("Pavel",2003,"Ekaterinburg")
    def test_correct_name(self):
        self.assertTrue(self.person.get_name() == self.name )
    def test_correct_age(self):
        age = self.person.get_age()
        self.assertTrue(self.person.get_age() == 20 )
    def test_correct_address(self):
        self.assertTrue(self.person.get_address() == self.address )
    def test_set_name(self):
        self.person.set_name("Pavel2")
        self.assertTrue(self.person.get_name() == "Pavel2")
    def test_set_address(self):
        self.person.set_address("Revda")
        self.assertTrue((self.person.get_address() == "Revda"))
    def test_is_homeless(self):
        self.assertTrue((self.person.is_homeless() == False))

