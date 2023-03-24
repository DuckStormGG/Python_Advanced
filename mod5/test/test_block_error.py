import unittest
from mod5.block_error import BlockErrors

class TestBlockError(unittest.TestCase):
    def test_blocking_error_correct(self):
        result = True
        try:
            with BlockErrors({ZeroDivisionError}):
                a = 1 / 0
        except:
            result = False
        self.assertTrue(result)
    def test_error_go_up(self):
        try:
            with BlockErrors({TypeError}):
                a = 1 / 0
        except Exception as e:
            if type(e) == ZeroDivisionError:
                self.assertTrue(True)
            else:
                self.assertTrue(False)




    def test_error_ignore_in_outer_block(self):
        result = True
        try:
            with BlockErrors({TypeError}):
                with BlockErrors({ZeroDivisionError}):
                    a = 1 / "0"
        except:
            result = False
        self.assertTrue(result)

