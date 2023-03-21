import unittest
import time
from mod5.runcode import app

# 2 задание
class TestRuncode(unittest.TestCase):
    def setUp(self) -> None:
        self.client = app.test_client()
        self.url = "/run-python"

    def test_timeout(self):
        start = time.time()
        self.client.post(self.url, data={"code": "import time\ntime.sleep(10)", "timeout": 5})
        self.assertTrue(6 > time.time() - start >= 5)

    def test_code_none(self):
        self.assertTrue(self.client.post(self.url, data={"code": "", "timeout": 5}).status_code == 400)

    def test_timeout_zero(self):
        self.assertTrue(
            self.client.post(self.url, data={"code": 'print()"; echo "hacked', "timeout": 0}).status_code == 400)

    def test_unsafe_input(self):
        test = self.client.post(self.url,
                                data={"code": "from subprocess import run\nrun(['./kill_the_system.sh'])",
                                      "timeout": 30}).data.decode()
        self.assertTrue("BlockingIOError" in test)
