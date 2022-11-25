import unittest
import os
import sys
from src.telecom_translate import Tenure

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

class TestTenure(unittest.TestCase):
    """
    tests tenure_avg() method
    """

    def test_10_entry(self):
        """
        Test case 1 using telecom_10user.txt with 10 row of data
        """
        input1 = './data/telecom_10users.txt'
        devs_obj = Tenure(input1)
        actual_result = devs_obj.tenure_avg()
        expected_result = {"Senior_months": 18,"NonSenior_months": 43.89,
                            "Senior_total": 1, "NonSenior_total": 9}
        self.assertDictEqual(actual_result, expected_result)

    def test_50_entry(self):
        """
        Test case 2 using telecom_50user.txt with 50 row of data
        """
        input1 = './data/telecom_50users.txt'
        devs_obj = Tenure(input1)
        actual_result = devs_obj.tenure_avg()
        expected_result = {"Senior_months": 42.71,"NonSenior_months": 34.86,
                            "Senior_total": 7, "NonSenior_total": 43}
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()