import unittest

from operations import operate

class TestStringMethods(unittest.TestCase):

    def test_operate(self):
        out = """    1
        *2 (=2)
        *4 (=8)
        *5 (=40)
        *3 (=120)
        -----------
total = 120 (mulitplication)"""

        exp = operate([1, 2, 4, 5, 3], "*")
        self.assertEqual(out, exp)


    
if __name__ == '__tests__':
    unittest.main()
