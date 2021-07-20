import unittest
from math import pi
from project.sample_codes import add2num, pow2num

class TestAdd2Num(unittest.TestCase):
    
    def test_addwithposs(self):
        self.assertEqual(add2num(8,4), 12)
    def test_addwithneg(self):
        self.assertEqual(add2num(-19, 10), -9)

class TestPow2Num(unittest.TestCase):
    
    def test_poss_pow(self):
        self.assertEqual(pow2num(3,4), 81)
    def test_neg_pow(self):
        self.assertAlmostEqual(pow2num(3, -3), 3**-3)

