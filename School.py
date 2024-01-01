'''
class School

This program creates a School class that records the description of the schools including names and location.
'''
from Park import Park

class School:
    '''
    A class to represent a school.
    Attributes:
        name: str
            name of the school
        latitude: float
            latitude of the school
        longitude: float
            longitude of the school
    Methods:
        distance(other_location): This method calculates the distance between the school and the park
        __str__(): This method creates a string representation of the School instances
        __eq__(other_location): The method checks whether two schools are in the same location
    '''
    def __init__(self, name, latitude, longitude):
        '''
        Name/Purpose: This method is a constructor and returns an object implicitly with stated attribute to the school.
        Parameter: A string represents the name of the school and two floats represent the latitude and longitude of the school respectively
        Return: An object implicitly with stated attribute of a School
        Raises/Throws: A type error will be raised if the name for the school is not a string, a type errors will be raised if latitude is not a float and a type errors will be raised if longitude is not a float. A value error will be raised if the latitude is smaller than -90.0 and larger than 90.0 and the longitude is smaller than -180.0 and larger than 180.0
        '''
        if not isinstance(name, str):
            raise TypeError("The name of a school should be a string!")
        self.name = name
        if not isinstance(latitude, float) or not isinstance(longitude, float):
            raise TypeError("The latitude and longitude of a school should be floats!")
        if latitude < -90.0 or latitude > 90.0:
            raise ValueError("The latitude is out of range.")
        if longitude < -180.0 or longitude > 180.0:
            raise ValueError("The longitude is out of range.")    
        self.latitude = latitude
        self.longitude = longitude

    def distance(self, other_location):
        '''
        Name/Purpose: This method calculates the distance between the school and the park
        Parameter: A Park object
        Return: A float represents the distance betwwen the school and the park
        Raises/Throws: A type error will be raised if the other location passed in is not a Park object
        '''
        if not isinstance(other_location, Park):
            raise TypeError("Please get a Park object for the distance calculation.")
        distance = ((self.latitude - other_location.latitude) ** 2 + (self.longitude - other_location.longitude) ** 2) ** 0.5
        return distance

    def __str__(self):
        '''
        Name/Purpose: This method creates a string representation of the School instances
        Parameter: None
        Return: A string
        Raises/Throws: None
        '''
        output = self.name + " with the latitude of " + str(self.latitude) + " and the longitude of " + str(self.longitude)
        return output

    def __eq__(self, other_location):
        '''
        Name/Purpose: The method checks whether two schools are in the same location
        Parameter: A School object
        Return: A boolean represent whether the two school are in the same location
        Raises/Throws: A type error will be raised if the the other location passed in is not a School object
        '''
        if not isinstance(other_location, School):
            raise TypeError("Please get a School object for comparison.")
        if self.latitude == other_location.latitude and self.longitude == other_location.longitude:
            return True
        else:
            return False
