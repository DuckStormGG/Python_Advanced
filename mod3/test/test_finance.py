import unittest

from mod3.finance import app


class TestFinanceAdd(unittest.TestCase):
    def setUp(self) -> None:
        app.config['Testing'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.base_url = '/add/'
    def tearDown(self) -> None:
        self.app.delete()

    def test_add_250(self):
        test_date = "20230312/"
        test_summ = "250"
        self.assertTrue( self.app.get(self.base_url + test_date + test_summ).status_code == 200)

    def test_add_wrong_number(self):
        test_date = "20230312/"
        test_summ = "asd"
        self.assertTrue(self.app.get(self.base_url + test_date + test_summ).status_code == 404)

    def test_add_negative_wont_work(self):
        test_date = "20230312/"
        test_summ = "-250"
        self.app.get(self.base_url + test_date + test_summ)
        self.assertTrue(self.app.get(self.base_url + test_date + test_summ).status_code == 404)
    def test_wrong_dateformat(self):
        test_date = "2023-03-12/"
        test_summ = "-250"
        self.app.get(self.base_url + test_date + test_summ)
        self.assertTrue(self.app.get(self.base_url + test_date + test_summ).status_code == 404)

class TestFinanceCalculate(unittest.TestCase):
    def setUp(self) -> None:
        app.config['Testing'] = True
        app.config['DEBUG'] = True
        self.app = app.test_client()
        self.app.get("/add/20000313/250")
        self.base_url = '/calculate/'
    def test_calculate_year(self):
        self.assertTrue(self.app.get(self.base_url +"2000").status_code == 200)
    def test_calculate_year_month(self):
        self.assertTrue(self.app.get(self.base_url +"2000"+"/03").status_code == 200)
    def test_calculate_year_without_data(self):
        with self.assertRaises(KeyError):
            self.assertTrue(self.app.get(self.base_url +"2022"))
    def test_calculate_year_month_without_data(self):
        with self.assertRaises(KeyError):
            self.assertTrue(self.app.get(self.base_url +"2022"+"/10"))
    def test_calculate_year_correct_number(self):
        result = self.app.get(self.base_url +"2023").data.decode()
        self.assertTrue(result == "250")
    def test_calculate_year_month_correct_number(self):
        result = self.app.get(self.base_url +"2023"+"/03").data.decode()
        self.assertTrue(result == "250")




