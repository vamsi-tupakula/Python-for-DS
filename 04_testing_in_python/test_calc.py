import unittest
import calc

"""
@imp NOTE : names of testing module and testing methods must start with 'test_'

@imp NOTE : How to run test_ file ?
python -m unittest test_calc.py
"""

class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10,5)
        self.assertEqual(result, 15)