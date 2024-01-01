'''
class Park

This program creates a Park class that records the description of the parks including names, location and facilities.
'''

class Park:
    '''
    A class to represent a park.
    Attributes:
        name: str
            name of the park
        latitude: float
            latitude of the park
        longitude: float
            longitude of the park
        facilities: dictionary
            facilities categories and counts in the park
    Methods:
        check_facility_exist(facility): The method checks whether the park has the facility in it
        __str__(): This method creates a string representation of the Park instances
        __eq__(other_location): The method checks whether two parks are in the same location
    '''
    
    def __init__(self, name, latitude, longitude, facilities):
        '''
        Name/Purpose: This function is a constructor and returns an object implicitly with stated attribute to the park.
        Parameter: A string represents the name of the park, two floats represent the latitude and longitude of the park respectively, and a dictionary represents the facilities included in the park as the keys and their counts as the value.
        Return: An object implicitly with stated attribute of a Park
        Raises/Throws: A type error will be raised if the name for the school is not a string, a type errors will be raised if latitude is not a float, a type errors will be raised if longitude is not a float and a type value will be raised if the facilities attribute is not a dictionary. A value error will be raised if the latitude is smaller than -90.0 and larger than 90.0 and the longitude is smaller than -180.0 and larger than 180.0
        '''
        if not isinstance(name, str):
            raise TypeError("The name of a park should be a string!")
        self.name = name
        if not isinstance(latitude, float) or not isinstance(longitude, float):
            raise TypeError("The latitude and longitude of a park should be floats!")
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("The latitude is out of range.")
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("The longitude is out of range.")
        self.latitude = latitude
        self.longitude = longitude
        if not isinstance(facilities, dict):
            raise TypeError("The facilities of a park should be stored in a dictionary!")
        self.facilities = facilities

    def check_facility_exist(self, facility):
        '''
        Name/Purpose: The method checks whether the park has the facility in it
        Parameter: A string represents the name of the facility
        Return: A boolean represents whether the park has such facility
        Raises/Throws: A type error will be raised if the name for the facility is not a string
        '''
        if not isinstance(facility, str):
            raise TypeError("The name of the facility should be a string.")
        for park_facility in self.facilities.keys():
            if facility == park_facility:
                return True
        return False

    def __str__(self):
        '''
        Name/Purpose: This method creates a string representation of the Park instances
        Parameter: None
        Return: A string
        Raises/Throws: None
        '''
        facilities_list = []
        for facility, count in self.facilities.items():
            facilities_list.append(str(count) + " " + facility)
        facilities = ", ".join(facilities_list)
        output = self.name + " with the latitude of " + str(self.latitude) + " and the longitude of " + str(self.longitude) + ". And the park has " + facilities
        return output

    def __eq__(self, other_location):
        '''
        Name/Purpose: The method checks whether two parks are in the same location
        Parameter: A Park object
        Return: A boolean represent whether the two park are in the same location
        Raises/Throws: A type error will be raised if the the other location passed in is not a Park object
        '''
        if not isinstance(other_location, Park):
            raise TypeError("Please get a Park object for comparison.")
        if self.latitude == other_location.latitude and self.longitude == other_location.longitude:
            return True
        else:
            return False