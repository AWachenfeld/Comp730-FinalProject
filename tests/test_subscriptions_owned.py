import unittest
import os
import sys
from src.telecom_translate import Subscriptions

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


class TestSubscriptionsOwned(unittest.TestCase):
    """
    tests the subscriptions_owned() method
    """

    def test_10_entry(self):
        """
        Test case 1 using telecom_10user.txt with 10 row of data
        """
        input1 = './data/telecom_10users.txt'
        devs_obj = Subscriptions(input1)
        actual_result = devs_obj.subscriptions_owned()
        expected_result = {"3_owned": 5, "2_owned": 2, "1_owned": 3}
        self.assertDictEqual(actual_result, expected_result)

    def test_50_entry(self):
        """
        Test case 2 using telecom_50user.txt with 50 row of data
        """
        input1 = './data/telecom_50users.txt'
        devs_obj = Subscriptions(input1)
        actual_result = devs_obj.subscriptions_owned()
        expected_result = {"3_owned": 23, "2_owned": 13, "1_owned": 14}
        self.assertDictEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()