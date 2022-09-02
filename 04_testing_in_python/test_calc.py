import unittest
import calc

"""
@imp NOTE : names of testing module and testing methods must start with 'test_'

@imp NOTE : How to run test_ file ?
python -m unittest test_calc.py
"""

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    def test_sub(self):
        self.assertEqual(calc.sub(10,5), 5)

    def test_mul(self):
        self.assertEqual(calc.mul(10,5), 50)
    
    def test_divide(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertRaises(ValueError, calc.divide, 10, 0)

if __name__ == '__main__':
    unittest.main()