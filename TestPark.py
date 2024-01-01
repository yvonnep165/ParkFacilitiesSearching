'''
Testing Park

This program creates a ParkTest class that tests the Park class
'''

import unittest
from Park import Park
from School import School

class ParkTest(unittest.TestCase):
    def test_init_basic(self):
        park = Park("Arbutus Village Park", 49.1234, -123.4637, {"Softball":2, "Wading Pool":1, "Tennis Courts":12})
        self.assertEqual(park.name, "Arbutus Village Park")
        self.assertEqual(park.latitude, 49.1234)
        self.assertEqual(park.longitude, -123.4637)
        self.assertEqual(park.facilities, {"Softball":2, "Wading Pool":1, "Tennis Courts":12})

    def test_not_string_park_name(self):
        with self.assertRaises(TypeError):
            park_name_not_string = Park(123, 50.14, 122.34, {"Restarant":4, "Running Tracks":11, "Soccer Fields":3})

    def test_not_float_latitude(self):
        with self.assertRaises(TypeError):
            park_latitude_integer = Park("abc", 3, 98.34, {"Softball":3, "Tennis court":60})
        with self.assertRaises(TypeError):
            park_latitude_string = Park("abc", "5.67", 98.34, {"Softball":3, "Tennis court":60})

    def test_not_float_longitude(self):
        with self.assertRaises(TypeError):
            park_longitude_integer = Park("efgk", 12.345, 65, {"Playgrounds":6, "Community Hall":8})
        with self.assertRaises(TypeError):
            park_longitude_string = Park("qwer", 34.654, "432", {"Playgrounds":6, "Community Hall":8})

    def test_not_dictionary_facilities(self):
        with self.assertRaises(TypeError):
            park_facilities_not_dictionary = Park("abcfe", 80.543, 24.636, ["Playgrounds", 6, "Community Hall", 10])

    def test_out_of_range_latitude(self):
        with self.assertRaises(ValueError):
            park_small_latitude = Park("Abc", -90.01, -123.4637, {"Softball":2, "Wading Pool":1, "Tennis Courts":12})
        with self.assertRaises(ValueError):
            park_large_latitude = Park("Efg", 90.01, -123.4637, {"Softball":2, "Wading Pool":1, "Tennis Courts":12})

    def test_out_of_range_longitude(self):
        with self.assertRaises(ValueError):
            park_small_longitude = Park("Abc", -45.65, -180.001, {"Softball":2, "Wading Pool":1, "Tennis Courts":12})
        with self.assertRaises(ValueError):
            park_large_longitude = Park("Efg", 75.345, 180.01, {"Softball":2, "Wading Pool":1, "Tennis Courts":12})

    def test_check_facility_exist_not_string(self):
        park_check_not_string_facility = Park("a park", 84.345, 124.234, {"facility":1, "running track": 3})
        with self.assertRaises(TypeError):
            park_check_not_string_facility.check_facility_exist(123)

    def test_check_facility_exist(self):
        park_check_facility = Park("park b", -65.46, 112.543, {"Softball":43, "Basketball Court": 12, "Playground":3})
        self.assertTrue(park_check_facility.check_facility_exist("Basketball Court"))
        self.assertFalse(park_check_facility.check_facility_exist("Running Track"))

    def test_string_representation(self):
        park_to_display = Park("parkabc", 43.65, -126.43, {"Basketball Court": 1, "Playground":5})
        self.assertEqual(park_to_display.__str__(), "parkabc with the latitude of 43.65 and the longitude of -126.43. And the park has 1 Basketball Court, 5 Playground")

    def test_eq_not_park_object_comparison(self):
        park_compare_with_not_park_object = Park("afd park", -43.45, -134.2, {"tennis court":2, "soccer field":5})
        with self.assertRaises(TypeError):
            park_compare_with_not_park_object.__eq__("afd park")
        with self.assertRaises(TypeError):
            park_compare_with_not_park_object.__eq__(School("afd park", -43.45, -134.2))

    def test_eq_same_park(self):
        park = Park("qwert park", 23.45, 143.43, {"tennis court":3})
        park_exact_same = Park("qwert park", 23.45, 143.43, {"tennis court":3})
        park_in_the_same_location_with_different_name_and_facility = Park("a park", 23.45, 143.43, {"soccer field":4})
        self.assertTrue(park.__eq__(park_exact_same))
        self.assertTrue(park.__eq__(park_in_the_same_location_with_different_name_and_facility))

    def test_eq_different_park(self):
        park = Park("qwert park", 23.45, 143.43, {"tennis court":3})
        park_complete_different = Park("red park", 54.23, 175.34, {"facility":32, "Playground":2})
        self.assertFalse(park.__eq__(park_complete_different))
        park_with_different_location = Park("qwert park", -34.6, 134.4, {"tennis court":3})
        self.assertFalse(park.__eq__(park_with_different_location))
        park_with_different_latitude = Park("qwert park", -34.87, 143.43, {"tennis court":3})
        self.assertFalse(park.__eq__(park_with_different_latitude))
        park_with_different_longitude = Park("qwert park", 23.45, 65.6592, {"tennis court":3})
        self.assertFalse(park.__eq__(park_with_different_longitude))

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()