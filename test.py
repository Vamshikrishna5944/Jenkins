import unittest
from lcm_compute import compute_lcm
class Testcompute_lcm(unittest.TestCase):
    def test_fact1(self):
        result = compute_lcm(2,4)
        self.assertEqual(result,4)
    def test_fact2(self):
        result = compute_lcm(7,12)
        self.assertEqual(result,84)
    def test_fact3(self):
        result = compute_lcm(5,10)
        self.assertEqual(result,2)
    def test_fact4(self):
        result = compute_lcm(9,11)
        self.assertEqual(result,2001)
    def test_fact5(self):
        result = compute_lcm(8,16)
        self.assertEqual(result,16)

if __name__ == '__main__':
    unittest.main()