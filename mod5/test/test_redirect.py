import sys
import unittest
import traceback
from mod5.redirect import Redirect


class TestRedirect(unittest.TestCase):
    def test_stdout(self):
        with open('stdout_test.txt', 'w') as stdout_file:
            with Redirect(stdout=stdout_file):
                print("TEST")
        with open('stdout_test.txt', 'r') as stdout_file:
            self.assertTrue("TEST" == stdout_file.read().replace("\n",''))

    #  не могу понять как проверить stderr

    # def test_stderr(self):
    #     tb = ''
    #     with open('stderr_test.txt', 'w') as stderr_file:
    #         try:
    #             with Redirect(stderr=stderr_file):
    #                 raise E
    #         except Exception as ex:
    #             tb = (''.join(traceback.TracebackException.from_exception(ex).format()))
    #     with open('stderr_test.txt', 'r') as stderr_file:
    #         self.assertTrue(stderr_file.read() == tb)



