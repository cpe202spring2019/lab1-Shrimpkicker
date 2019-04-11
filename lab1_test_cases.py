import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter_with_all_different_values(self):
        """tests function max_list_iter with lists of various sizes, with all unique values.
        Simultaneously tests the function with the max value at different indexes in the lists"""
        self.assertEqual(max_list_iter([1,2,3]), 3)
        self.assertEqual(max_list_iter([2,3,5,4]), 5)
        self.assertEqual(max_list_iter([3,4,7,5,6]), 7)
        self.assertEqual(max_list_iter([1,4,2,3]), 4)
        self.assertEqual(max_list_iter([2,1]), 2)

    def test_max_list_iter_with_repetetive_values(self):
        """tests function max_list_iter with lists of various sizes, with repetitive values.
        Also tests the function with multiple maximum values and multiple minimum values
        at differing indexes"""
        self.assertEqual(max_list_iter([1,2,1]), 2)
        self.assertEqual(max_list_iter([1,1,2]), 2)
        self.assertEqual(max_list_iter([2,1,1]), 2)
        self.assertEqual(max_list_iter([1,2,2,2]), 2)
        self.assertEqual(max_list_iter([2,1,2,2]), 2)
        self.assertEqual(max_list_iter([2,2,1,2]), 2)
        self.assertEqual(max_list_iter([3,3]), 3)

    def test_max_list_iter_with_none_list(self):
        """tests function max_list_iter with a list equal to None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter_with_empty_list(self):
        """tests function max_list_iter with an empty list"""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_reverse_rec(self):
        """tests function reverse_rec with lists of various sizes"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,3,4]), [4,3,2,1])
        self.assertEqual(reverse_rec([3,4,5,6,7]), [7,6,5,4,3])
        
    def test_reverse_rec_with_none_list(self):
        """tests function reverse_rec with a list equal to None"""
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_bin_search(self):
        """tests function bin_search with one list and multiple low/high values"""
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(bin_search(4, 0, 10, list_val), 4)
        self.assertEqual(bin_search(6, 0, 8, list_val), 6)
        self.assertEqual(bin_search(8, 4, 10, list_val), 8)
        
    def test_bin_search_with_none_list(self):
        """tests function bin_search with a list equal to None"""
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(0,0,0,tlist)

    def test_bin_search_with_nonexistent_values(self):
        """tests function bin_search with values that aren't in the list and with values that aren't in the slice of the list
        (values that aren't between the indexes high and low given"""
        list_val = [0,2,3,5]
        self.assertEqual(bin_search(4, 0, 3, list_val), None)
        self.assertEqual(bin_search(1, 0, 3, list_val), None)
        self.assertEqual(bin_search(6, 0, 3, list_val), None)
        self.assertEqual(bin_search(5, 0, 2, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
