'''
Testing School

This program creates a SchoolTest class that tests the School class
'''

import unittest
from School import School
from Park import Park

class SchoolTest(unittest.TestCase):
    def test_init_basic(self):
        school = School("Elsie Roy Elementary", 49.27223, -123.1224)
        self.assertEqual(school.name, "Elsie Roy Elementary")
        self.assertEqual(school.latitude, 49.27223)
        self.assertEqual(school.longitude, -123.1224)

    def test_not_string_school(self):
        with self.assertRaises(TypeError):
            school_name_not_string = School(435, 34.324, 124.54)

    def test_not_float_latitude(self):
        with self.assertRaises(TypeError):
            school_latitude_integer = School("school a", 3, 124.345)
        with self.assertRaises(TypeError):
            school_latitude_string = School("school b", "23.45", 54.34)

    def test_not_float_longitude(self):
        with self.assertRaises(TypeError):
            school_longitude_integer = School("school c", -43.54, 63)
        with self.assertRaises(TypeError):
            school_longitude_string = School("school d", 65.98, "145.4")

    def test_out_of_range_latitude(self):
        with self.assertRaises(ValueError):
            school_small_latitude = School("Academy", -90.01, -155.43)
        with self.assertRaises(ValueError):
            school_large_latitude = School("campus", 90.01, -125.346)

    def test_out_of_range_longitude(self):
        with self.assertRaises(ValueError):
            school_small_longitude = School("Abc", 54.56, -180.001)
        with self.assertRaises(ValueError):
            school_large_longitude = School("Efg", 85.45, 180.01)
    
    def test_distance_with_not_park(self):
        school_distance_with_non_park = School("Fraser Academy", 12.45, -134.4543)
        with self.assertRaises(TypeError):
            school_distance_with_non_park.distance("Fraser Academy")
        with self.assertRaises(TypeError):
            school_distance_with_non_park.distance(School("John Henderson Elementary", 3.45, -129.456))

    def test_distance(self):
        school = School("Lord Roberts Annex", -67.32, -143.98)
        self.assertAlmostEqual(school.distance(Park("Park abc", 35.65, -86.54, {"Tennis court":12, "Running track":43})), 117.90748279901491)

    def test_string_representation(self):
        school_to_display = School("Madrona School", 46.56, 175.654)
        self.assertEqual(school_to_display.__str__(), "Madrona School with the latitude of 46.56 and the longitude of 175.654")

    def test_eq_not_school_object_comparison(self):
        school_compare_with_not_school_object = School("xyz school", 23.34, 68.76)
        with self.assertRaises(TypeError):
            school_compare_with_not_school_object.__eq__("xyz school")
        with self.assertRaises(TypeError):
            school_compare_with_not_school_object.__eq__(Park("abc park", 23.34, 68.76, {"softball":15, "basketball court":4}))

    def test_eq_same_school(self):
        school = School("St John's School", 49.2631, -123.1562)
        school_exact_same = School("St John's School", 49.2631, -123.1562)
        school_in_the_same_location_with_different_name = School("cdef School", 49.2631, -123.1562)
        self.assertTrue(school.__eq__(school_exact_same))
        self.assertTrue(school.__eq__(school_in_the_same_location_with_different_name))
    
    def test_eq_different_school(self):
        school = School("Henry Hudson Elementary", 43.56, 135.86)
        school_complete_different = School("John Academy", 45.345, 143.853)
        self.assertFalse(school.__eq__(school_complete_different))
        school_with_different_location = School("Henry Hudson Elementary", 43.57, 135.65)
        self.assertFalse(school.__eq__( school_with_different_location))
        school_with_different_latitude = School("Henry Hudson Elementary", -12.45, 135.86)
        self.assertFalse(school.__eq__( school_with_different_latitude))
        school_with_different_longitude = School("Henry Hudson Elementary", 45.56, 163.987)
        self.assertFalse(school.__eq__( school_with_different_longitude))

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()