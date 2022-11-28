import unittest
import os
import sys
from src.telecom_translate import Contractrenewal

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


class TestContractRenewal(unittest.TestCase):
    """
    tests contract_reneval() method
    """

    def test_10_entry(self):
        """
        Test case 1 using telecom_10user.txt with 10 row of data
        """
        input1 = './data/telecom_10users.txt'
        devs_obj = Contractrenewal(input1)
        actual_result = devs_obj.contract_renewal()
        expected_result = {'NonSenior_cancel': 2, 'NonSenior_renew': 7,
                           'Senior_cancel': 1, 'Senior_renew': 0}

        self.assertDictEqual(actual_result, expected_result)

    def test_50_entry(self):
        """
        Test case 2 using telecom_50user.txt with 50 row of data
        """
        input1 = './data/telecom_50users.txt'
        devs_obj = Contractrenewal(input1)
        actual_result = devs_obj.contract_renewal()
        expected_result = {'NonSenior_cancel': 15, 'NonSenior_renew': 28,
                           'Senior_cancel': 3, 'Senior_renew': 4}
        self.assertDictEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()
