import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_wit_none_list(self):
        """tests function max_list_iter with a list equal to None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        #self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        pass

    def test_bin_search(self):
        '''list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )'''
        pass

if __name__ == "__main__":
        unittest.main()

    
