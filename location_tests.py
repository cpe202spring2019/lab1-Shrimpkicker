import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """tests the return value for the __repr__ of a Location object"""
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):
        """tests the return value for the __eq__ of a Location object with other Location objects"""
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)
        loc3 = Location("SLO", 35.3, -120.7)
        loc4 = loc1

        self.assertTrue(loc1 == loc3)
        self.assertFalse(loc1 == loc2)
        self.assertTrue(loc1 == loc4)
        self.assertTrue(loc3 == loc4)

    def test_init_values(self):
        """tests the return values for the initialized methods of Location objects"""
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("Paris", 48.9, 2.4)

        self.assertEqual(loc1.name, 'SLO')
        self.assertEqual(loc1.lat, 35.3)
        self.assertEqual(loc1.lon, -120.7)
        self.assertEqual(loc2.name, 'Paris')
        self.assertEqual(loc2.lat, 48.9)
        self.assertEqual(loc2.lon, 2.4)

if __name__ == "__main__":
        unittest.main()
