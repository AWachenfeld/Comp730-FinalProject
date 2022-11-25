import unittest
import os
import sys
from src.telecom_translate import Monthlycharges

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

class TestMonthlyCharges(unittest.TestCase):
    """
    tests monthly_charges() method
    """

    def test_10_entry(self):
        """
        Test case 1 using telecom_10user.txt with 10 row of data
        """
        input1 = './data/telecom_10users.txt'
        devs_obj = Monthlycharges(input1)
        actual_result = devs_obj.monthly_charges()
        expected_result = {"Senior_charges": 84.95,"NonSenior_charges": 67.73,
                            "Senior_total": 1, "NonSenior_total": 9}
        self.assertDictEqual(actual_result, expected_result)

    def test_50_entry(self):
        """
        Test case 2 using telecom_50user.txt with 50 row of data
        """
        input1 = './data/telecom_50users.txt'
        devs_obj = Monthlycharges(input1)
        actual_result = devs_obj.monthly_charges()
        expected_result = {"Senior_charges": 87.54,"NonSenior_charges": 65.45,
                            "Senior_total": 7, "NonSenior_total": 43}
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()