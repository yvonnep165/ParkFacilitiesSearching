'''
Testing Data Dashboard

This program creates a Data_Dashboard_Test class that tests the funtions in Data Dashboard.
'''

import unittest
from School import School
from Park import Park
from data_dashboard import *

CONTENT_TEST_INDEX = 20

class Data_Dashboard_Test(unittest.TestCase):
    def test_download_data_error(self):
        with self.assertRaises(Exception):
            download_data("rewfdsfv")
    
    def test_download_data(self):
        content = download_data("https://opendata.vancouver.ca/explore/dataset/schools/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B")
        self.assertEqual(content[:CONTENT_TEST_INDEX], "ADDRESS;SCHOOL_CATEG")

    def test_get_contect_row_not_string(self):
        with self.assertRaises(TypeError):
            content_with_number = get_content_row(123)
        with self.assertRaises(TypeError):
            content_of_list = get_content_row([123, "school"])

    def test_get_content_row(self):
        self.assertEqual(get_content_row("this\nis\na\n137\nschool"), ["this", "is" , "a" , "137", "school"])

    def test_get_school_detail_empty(self):
        with self.assertRaises(ValueError):
            school_detail_empty_list = get_school_detail([])

    def test_get_school_detail_not_list(self):
        with self.assertRaises(TypeError):
            school_detail_in_number = get_school_detail(2434)
        with self.assertRaises(TypeError):
            school_detail_in_string = get_school_detail("abc academy, 14.453, 143.453")
        with self.assertRaises(TypeError):
            school_detail_in_dictionary = get_school_detail({"abc academy": [14.453, 143.453]})

    def test_get_school_detail(self):
        school_detail = get_school_detail(['Title', '688 W Hastings St;Independent School;Alexander Academy;"{""coordinates\"": [-123.11400985419304, 49.28500059925005], ""type"": ""Point""}";Downtown','5025 Willow St;Public School;BC Children\'s Adol. Psych. Unit;'])
        self.assertEqual(school_detail, {"Alexander Academy":[-123.11400985419304, 49.28500059925005]})

    def test_get_school_object_not_dictionary(self):
        with self.assertRaises(TypeError):
            get_school_object(["Sir Alexander Mackenzie Elementary", -123.08671432, 49.23453643506752])
        with self.assertRaises(TypeError):
            get_school_object("Sir Alexander Mackenzie Elementary")
        with self.assertRaises(TypeError):
            get_school_object(-123.08671432)

    def test_get_school_object(self):
        school = get_school_object({"Sir Alexander Mackenzie Elementary": [-123.08671432, 49.23453643506752]})
        self.assertEqual(school, [School("Sir Alexander Mackenzie Elementary", 49.23453643506752, -123.08671432)])

    def test_get_park_location_empty(self):
        with self.assertRaises(ValueError):
            park_location_empty_list = get_park_location([])

    def test_get_park_location_not_list(self):
        with self.assertRaises(TypeError):
            park_location_in_number = get_park_location(5436)
        with self.assertRaises(TypeError):
            park_location_in_string = get_park_location("abc park, 14.453, 143.453")
        with self.assertRaises(TypeError):
            park_location_in_dictionary = get_park_location({"abc park": [14.453, 143.453]})

    def test_get_park_location(self):
        park_location = get_park_location(['Title', '133;China Creek North Park;1;N;N;Y;N;1001;E 7th Avenue;E 7th Avenue;Glen Drive;Mount Pleasant;https://vancouver.ca/news-calendar/mount-pleasant.aspx;3.16;49.264901,-123.083355','237;Yaletown Park;1;N;N;N;N;901;Mainland Street;Mainland Street;Nelson Street;Downtown;website;0.17;49.277042,-123.118921', '231;Camosun;0;N;N;N;N;4102;W 16th Avenue;W 16th Avenue;Discovery Street;Dunbar-Southlands;'])
        self.assertEqual(park_location, {"China Creek North Park" : [49.264901, -123.083355]})

    def test_get_park_facilities_detail_empty(self):
        with self.assertRaises(ValueError):
            facilities_empty_list = get_park_facilities_detail([])

    def test_get_park_facilities_detail_not_list(self):
        with self.assertRaises(TypeError):
            park_facilities_in_number = get_park_facilities_detail(375)
        with self.assertRaises(TypeError):
            park_facilities_in_string = get_park_facilities_detail("abc park, tennis court, 1")
        with self.assertRaises(TypeError):
            park_facilities_in_dictionary = get_park_facilities_detail({"abc park": ["softball", 4]})

    def test_get_park_object_park_detail_not_dictionary(self):
        with self.assertRaises(TypeError):
            park_detail_in_number = get_park_object(5673, {"Oak Park" : {"Soccer Fields" : 3}})
        with self.assertRaises(TypeError):
            park_detail_in_string = get_park_object("abc park, 43.45, 123.453", {"abc Park" : {"Tennis Court" : 5}})
        with self.assertRaises(TypeError):
            park_detail_in_list = get_park_object(["abc park", 43.45, 123.453], {"efg Park" : {"Softball" : 2}})

    def test_get_park_object_park_facilities_detail_not_dictionary(self):
        with self.assertRaises(TypeError):
            facilities_detail_in_number = get_park_object({"China Creek North Park" : [49.264901, -123.083355]}, 654.35)
        with self.assertRaises(TypeError):
            facilities_detail_in_string = get_park_object({"China Creek North Park" : [49.264901, -123.083355]}, "abc park, tennis court, 1")
        with self.assertRaises(TypeError):
            facilities_detail_in_list = get_park_object({"China Creek North Park" : [49.264901, -123.083355]}, ["abc park", "tennis court", 1])

    def test_get_park_object(self):
        park = get_park_object({"China Creek North Park" : [49.264901, -123.083355]}, {"China Creek North Park" : {"Soccer Fields" : 3}})
        self.assertEqual(park, [Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3})])

    def test_get_parks_with_facility_not_string_facility(self):
        park = [Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3})]
        with self.assertRaises(TypeError):
            facility_as_number = get_parks_with_facility(176, park)
        with self.assertRaises(TypeError):
            facility_as_list = get_parks_with_facility(["Tennis court"], park)
        with self.assertRaises(TypeError):
            facility_as_dictionary = get_parks_with_facility({"Tennis Court" : 3}, park)

    def test_get_parks_with_facility_not_park_object_list(self):
        park = Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3})
        with self.assertRaises(TypeError):
            park_object_list_not_list = get_parks_with_facility("Tennis Court", park)

    def test_get_parks_with_facility(self):
        parks = [Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3}), Park("abd Park", 54.45, -133.083355, {"Tennis" : 5})]
        parks_has_facility = get_parks_with_facility("Soccer Fields", parks)
        self.assertEqual(parks_has_facility, [Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3})])
        parks_no_requested_facility_list = [Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3}), Park("abd Park", 54.45, -133.083355, {"Tennis" : 5})]
        parks_no_requested_facility = get_parks_with_facility("Playgrounds", parks_no_requested_facility_list)
        self.assertEqual(parks_no_requested_facility, [])

    def test_get_user_school_object_not_string_school(self):
        school_list = [School("abc", 43.453, 143.342), School("efd", 54.432, 132.343)]
        with self.assertRaises(TypeError):
            school_name_number = get_user_school_object(8495, school_list)
        with self.assertRaises(TypeError):
            school_name_list = get_user_school_object(['abc'], school_list)

    def test_get_user_school_object_not_list(self):
        with self.assertRaises(TypeError):
            school_object_not_list = get_user_school_object("Alexander Academy", School("Alexander Academy", 34.243, 54.343))

    def test_get_user_school_object(self):
        school_object_list = [School("Alexander Academy", -24.453, -43.4726), School("abc academy", 59.543, 93.563)]
        school = get_user_school_object("Alexander Academy", school_object_list)
        self.assertEqual(school , School("Alexander Academy", -24.453, -43.4726))

    def test_get_list_of_closest_parks_with_facilities_not_school_object(self):
        parks_list = [Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3}), Park("abd Park", 54.45, -133.083355, {"Tennis" : 5}), Park("Stanley Park", 49.35, -123.0432355, {"Tennis" : 5})]
        with self.assertRaises(TypeError):
            list_of_closest_parks_with_string = get_list_of_closest_parks_with_facilities("abc school", parks_list)
        with self.assertRaises(TypeError):
            list_of_closest_parks_with_list_school = get_list_of_closest_parks_with_facilities(["abc school", "edf academy"], parks_list)

    def test_get_list_of_closest_parks_with_facilities_not_park_list(self):
        school = School("abc academy", 39.5437, 145.864)
        with self.assertRaises(TypeError):
            list_of_closest_parks_park_object_not_list = get_list_of_closest_parks_with_facilities(school, Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3}))

    def test_get_list_of_closest_parks_with_facilities(self):
        school = School("NEU", 3.45, 23.585)
        closest_park = Park("abc park", 12.343, 23.434, {"facility" : 1})
        second_closest_park = Park("efg park", 43.532, 64.243, {"facility" : 1})
        third_closest_park = Park("lmn park", 65.442, 100.424, {"facility" : 1})
        not_close_park = Park("xyz park", 89.748, 173.4432, {"facility" : 1})
        three_closest_parks = get_list_of_closest_parks_with_facilities(school, [closest_park, second_closest_park, third_closest_park, not_close_park])
        self.assertEqual(three_closest_parks, [closest_park, second_closest_park, third_closest_park])
        closet_parks_less_than_three = get_list_of_closest_parks_with_facilities(school, [closest_park, second_closest_park])
        self.assertEqual(closet_parks_less_than_three, [closest_park, second_closest_park])
        
    def test_display_closet_parks_with_facilities_not_school_object(self):
        parks_list = [Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3}), Park("abd Park", 54.45, -133.083355, {"Tennis" : 5}), Park("Stanley Park", 49.35, -123.0432355, {"Tennis" : 5})]
        with self.assertRaises(TypeError):
            display_list_of_closest_parks_with_string = display_closet_parks_with_facilities("abc school", parks_list)
        with self.assertRaises(TypeError):
            display_list_of_closest_parks_with_list_school = display_closet_parks_with_facilities(["abc school", "edf academy"], parks_list)

    def test_display_closet_parks_with_facilities_not_park_object_list(self):
        school = School("abc academy", 39.5437, 145.864)
        with self.assertRaises(TypeError):
            display_list_of_closest_parks_park_object_not_list = display_closet_parks_with_facilities(school, Park("China Creek North Park", 49.264901, -123.083355, {"Soccer Fields" : 3}))

def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()