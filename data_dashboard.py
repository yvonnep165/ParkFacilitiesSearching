'''
This program analyses three data sets: school, park and park facilities. The program cleans and parses the data into School objects and Park objects. 
For a student in any school located in Vancouver, the program filters the parks with the facility they want and calculates the distance between the school and these park. 
The program takes user input through a GUI where the student can choose his/her school and the requested facility from the drop down list. 
After that, the program shows the student the closest three parks where the student can find the facility they want and all the other facilites in those three parks in the terminal.
The program provides a bar graph showing the closest three parks with all the facilities and highlighting the requested facility. 
'''

import requests
import matplotlib.pyplot as plt 
from tkinter import *
from tkinter import ttk
from Park import Park
from School import School

DATA_TITLE_ROW_INDEX_ROW_INDEX = 1
SCHOOL_ENTRIES_LENGTH = 5
SCHOOL_LOCATION_COLUMN_INDEX = 3
SCHOOL_LATITUDE_INDEX = 1
SCHOOL_LONGITUDE_INDEX = 0
SCHOOL_LONGITUDE_INDEX_AFTER_SPLIT = 1
SCHOOL_NAME_COLUMN_INDEX = 2
PARK_ENTRIES_LENGTH = 15
FACILITIES_COLUMN_INDEX_IN_PARK = 5
NO_FACILITIES = "N"
PARK_LATITUDE_INDEX = 0
PARK_LONGITUDE_INDEX = 1
PARK_LOCATION_COLUMN_INDEX = 14
PARK_NAME_COLUMN_INDEX = 1
FACILITIES_ENTRIES_LENGTH = 5
PARK_COLUMN_INDEX_IN_FACILITIES = 1
FACILITIES_NAME_COLUMN_INDEX = 2
FACILITIES_COUNT_COLUMN_INDEX = 3
DEFAULT_NUMBER_OF_PARKS_DISPLAY = 3
INFINITE = float('inf')
FIRST_PARK_DIAPLAY_INDEX = 1
CEILING = 1
Y_COORDINATE_START_POINT = 0
FIGURE_SIZE_WIDTH = 12
FIGURE_SIZE_HEIGHT = 6
GRAPHS_ROW = 1
NUMBER_GRAPH_PER_ROW = 3
LABLE_ANGLE = 80
USER_FACILITY_BAR_COLOR = "red"
OTHER_BAR_COLOR = "blue"
global_school_var = ""
global_facility_var = ""

def download_data(website):
    '''
    Name/Purpose: This function allows the program to get the data from a website
    Parameter: A string represents the address of the website
    Return: A string represents the text of the website
    Raises/Throws: An HTTP Error will be raised if the website request returns an unsuccessful status code. If there's a network problem, a Connection Error will be raised.
    '''
    try:
        website  = requests.get(website)
        content = website.text
        return content
    except ConnectionError:
        print("These is a network problem.")
    except website.raise_for_status():
        print("The request was not successful and an error may have occurred")

def get_content_row(content):
    '''
    Name/Purpose: This function splits the website lines by lines and returns a list of data rows
    Parameter: A string represents the text of the website
    Return: A list of data rows
    Raises/Throws: A Type Error will be raised if the website content passed in is not a string
    '''
    if not isinstance(content, str):
        raise TypeError("The content should be a string.")
    content = content.split("\n")
    return content

def get_school_detail(school_list):
    '''
    Name/Purpose: This function gets the location, which includes latitude and longitude, of the school and store the details into a dictionary
    Parameter: A list of school data rows
    Return: A dictionary with the school's names as the keys and school's location as the value
    Raises/Throws: If the school list is empty, a value error will be raised. If the school list passed in is not a list, a type error will be raised.
    '''
    if len(school_list) < 1:
        raise ValueError("The school list is empty.")
    if not isinstance(school_list, list):
        raise TypeError("The school list needs to be a list.")
    school_detail = {} 
    for school in school_list[DATA_TITLE_ROW_INDEX_ROW_INDEX:]:
        school = school.split(";")
        if len(school) < SCHOOL_ENTRIES_LENGTH:
            continue
        latitude = float(school[SCHOOL_LOCATION_COLUMN_INDEX].split(",")[SCHOOL_LATITUDE_INDEX].strip("]"))
        longitude = float(school[SCHOOL_LOCATION_COLUMN_INDEX].split(",")[SCHOOL_LONGITUDE_INDEX].split(":")[SCHOOL_LONGITUDE_INDEX_AFTER_SPLIT].strip(" ["))
        school_position = [longitude, latitude]
        school_detail[school[SCHOOL_NAME_COLUMN_INDEX]] = school_position
    return school_detail

def get_school_object(school_detail):
    '''
    Name/Purpose: This function creates a list of School objects
    Parameter: A dictionary with the school's names as the keys and school's location as the value
    Return: A list of School objects
    Raises/Throws: If the school detail passed in is not a dictionary, a Type Error will be raised. 
    '''
    if not isinstance(school_detail, dict):
        raise TypeError("The school details passed in for School objects construction need to be a dictionary")
    school_object_list = []
    for school, position in school_detail.items():
        school_object_list.append(School(school, position[SCHOOL_LATITUDE_INDEX], position[SCHOOL_LONGITUDE_INDEX]))
    return school_object_list

def get_park_location(park_list):
    '''
    Name/Purpose: This function gets the location, which includes latitude and longitude, of the park and store the details into a dictionary
    Parameter: A list of park data rows
    Return: A dictionary with the park's names as the keys and park's location as the value
    Raises/Throws: If the park list is empty, a value error will be raised. If the park list passed in is not a list, a type error will be raised.
    '''
    if len(park_list) < 1:
        raise ValueError("The park list is empty.")
    if not isinstance(park_list, list):
        raise TypeError("The park list needs to be a list.")
    park_location = {}
    for park in park_list[DATA_TITLE_ROW_INDEX_ROW_INDEX:]:
        park = park.split(";")
        if len(park) < PARK_ENTRIES_LENGTH:
            continue
        if park[FACILITIES_COLUMN_INDEX_IN_PARK] == NO_FACILITIES:
            continue
        position = park[PARK_LOCATION_COLUMN_INDEX].split(",")
        latitude = float(position[PARK_LATITUDE_INDEX])
        longitude = float(position[PARK_LONGITUDE_INDEX])
        park_position = [latitude, longitude]
        park_location[park[PARK_NAME_COLUMN_INDEX]] = park_position
    return park_location

def get_park_facilities_detail(park_facilities_list):
    '''
    Name/Purpose: This function gets the facility details, which includes facilities categories and their counts, of each park and store the details into a dictionary
    Parameter: A list of park facilities data rows
    Return: A dictionary with the park's names as the keys and a dicionary (which includes the facilities category as key and each category counts as value) as value
    Raises/Throws: If the park facilities list is empty, a value error will be raised. If the park facilities list passed in is not a list, a type error will be raised.
    '''
    if len(park_facilities_list) < 1:
        raise ValueError("The park facilities list is empty.")
    if not isinstance(park_facilities_list, list):
        raise TypeError("The park facilities list needs to be a list.")
    park_facility = {}
    for facility in park_facilities_list[DATA_TITLE_ROW_INDEX_ROW_INDEX:]:
        facility = facility.split(";")
        if len(facility) < FACILITIES_ENTRIES_LENGTH:
            continue
        park = facility[PARK_COLUMN_INDEX_IN_FACILITIES].strip()
        if park not in park_facility.keys():
            park_facility[park] = {}
            park_facility[park][facility[FACILITIES_NAME_COLUMN_INDEX]] = int(facility[FACILITIES_COUNT_COLUMN_INDEX])
        else:
            park_facility[park][facility[FACILITIES_NAME_COLUMN_INDEX]] = int(facility[FACILITIES_COUNT_COLUMN_INDEX])
    return park_facility 

def get_park_object(park_detail, park_facilities_detail):
    '''
    Name/Purpose: This function creates a list of Park objects
    Parameter: A dictionary with the parks' names as the keys and parks' location as the value and A dictionary with the park's names as the keys and a dicionary (which includes the facilities category as key and each category counts as value) as value
    Return: A list of Park objects
    Raises/Throws: If the park detail passed in is not a dictionary, a Type Error will be raised. If the park facilities detail passed in is not a dictionary, a Type Error will be raised.
    '''
    if not isinstance(park_detail, dict):
        raise TypeError("The park details passed in for Park objects construction need to be a dictionary")
    if not isinstance(park_facilities_detail, dict):
        raise TypeError("The park facilities details passed in for Park objects construction need to be a dictionary")
    park_object_list = []
    for park, location in park_detail.items():
        latitude = location[PARK_LATITUDE_INDEX]
        longitude = location[PARK_LONGITUDE_INDEX]
        facilities = park_facilities_detail[park]
        park_object_list.append(Park(park, latitude, longitude, facilities))
    return park_object_list

##take in user input through a GUI element that has an impact on the data visulization
def get_user_school_and_facility(school_object_list, park_facilities_detail):
    '''
    Name/Purpose: This function takes user input through a GUI where the student can choose his/her school and the requested facility from the drop down list
    Parameter: A list of school object and a dictionary of park's names as keys with a dictionary of facilities and their counts as value
    Return: None
    Raises/Throws: None
    '''
    def school_selection(event):
        '''
        Name/Purpose: This function would be called when the school combobox selection was made, to assign the string variable to the global school variable called global_school_var
        Parameter: None
        Return: None
        '''
        global global_school_var
        global_school_var = school_combo.get()

    def facility_selection(event):
        '''
        Name/Purpose: This function would be called when the facility combobox selection was made, to assign the string variable to the global facility variable called global_facility_var
        Parameter: None
        Return: None
        '''
        global global_facility_var
        global_facility_var = facility_combo.get()

    def submit_to_generate_graph():
        '''
        Name/Purpose: This function would be called when the "submit" button was clicked, to close the widget
        Parameter: None
        Return: None
        '''
        root.destroy()
        
    root = Tk()
    root.geometry("400x350")
    label = ttk.Label(root, text = "As a student in any school in Vancouver, if you want to find a specific facility, this program will help you find the closest three parks where such a facility is available. Please choose your school and the facility you want. And you can see the parks with the requested facility and other facilities offered in the parks.")
    label.config(wraplength = 250)     
    label.config(justify = CENTER, anchor="center")
    label.pack(fill = BOTH, expand = True)

    school_name = []
    for school in school_object_list:
        school_name.append(school.name)
    ttk.Label(root, text = "Please choose your school").pack()
    school = StringVar()
    school_combo = ttk.Combobox(root, values=school_name, textvariable=school, state = 'readonly')
    school_combo.pack()
    school_combo.bind("<<ComboboxSelected>>",  school_selection)

    facility_name = []
    for park in park_facilities_detail.keys():
        for facility in park_facilities_detail[park].keys():
            if facility not in facility_name:
                facility_name.append(facility)
    ttk.Label(root, text = "Please choose your facility").pack()
    facility = StringVar()
    facility_combo = ttk.Combobox(root, values=facility_name, textvariable=facility, state = 'readonly')
    facility_combo.pack()
    facility_combo.bind("<<ComboboxSelected>>",  facility_selection)

    button = ttk.Button(root, text = "submit", command = submit_to_generate_graph)
    button.pack()

    root.mainloop()

def get_parks_with_facility(facility, park_object_list):
    '''
    Name: This function gets a list of parks which have the facility requested by the user
    Parameter: A string represents the user's requested facility and A list of Park objects
    Return: A list of Park objects
    Raises/Throws: If the facility is not a string or the park object list is not a list, a Type Error will be raised. 
    '''
    if not isinstance(facility, str):
        raise TypeError("The facility needs to be a string.")
    if not isinstance(park_object_list, list):
        raise TypeError("The park object list passed in needs to be a list.")
    parks_has_facility = []
    for park in park_object_list:
        if park.check_facility_exist(facility):
            parks_has_facility.append(park)
    return parks_has_facility

def get_user_school_object(school_name, school_object_list):
    '''
    Name/Purpose: This function gets the school object with the name of the user's school
    Parameter: A string represents the user's school and a list of School objects
    Return: A School instance
    Raises/Throws: If the school name is not a string or the school object list is not a list, a Type Error will be raised.
    '''
    if not isinstance(school_name, str):
        raise TypeError("The school name needs to be a string.")
    if not isinstance(school_object_list, list):
        raise TypeError("The school object list passed in needs to be a list.")
    for school in school_object_list:
        if school.name == school_name:
            return school

def get_list_of_closest_parks_with_facilities(school, parks_list):
    '''
    Name/Purpose: This function calculates the distance between the school and the parks and figures out the closest three parks. If there're less than three parks, the function still records the parks.
    Parameter: A School object and a list of Park objects filtered with the facility requested by the user
    Return: A list of Park objects
    Raises/Throws: If the school passed in is not a School object or the parks list is not a list, a Type Error will be raised.
    '''
    if not isinstance(school, School):
        raise TypeError("The school passed in needs to be a School object.")
    if not isinstance(parks_list, list):
        raise TypeError("The park object list passed in needs to be a list.")
    closest_three_parks = []
    number_of_parks_display = min(len(parks_list), DEFAULT_NUMBER_OF_PARKS_DISPLAY)
    for count in range(number_of_parks_display):
        closest_distance = INFINITE
        for park in parks_list:
            new_distance = school.distance(park)
            if new_distance <= closest_distance:
                closest_distance = new_distance
                closest_park = park
        closest_three_parks.append(closest_park)
        parks_list.pop(parks_list.index(closest_park))
    return closest_three_parks

def display_closet_parks_with_facilities(school, closest_parks):
    '''
    Name/Purpose: The function displays the closest parks from the user's school with the requested facility and displays all the facilities in those parks. The function displays three closest parks. But if there're less than three parks that have the facility the user wants, the function displays less than three parks. 
    Parameter: A School object and A list of Park objects
    Return: None
    Raises/Throws: If the school passed in is not a School object and the parks list is not a list, a Type Error will be raised.
    '''
    if not isinstance(school, School):
        raise TypeError("The school passed in needs to be a School object.")
    if not isinstance(closest_parks, list):
        raise TypeError("The closest parks passed in needs to be a list.")
    print(f"Your school is {school}. \nThe closest three parks with your requested facility are: ")
    park_display_number = FIRST_PARK_DIAPLAY_INDEX
    for park in closest_parks:
        print(f"{park_display_number}. {park}")
        park_display_number += 1

##create a bar graph based on the user's choices and the data analysis
def make_bar_graph_from_objects(closest_parks, user_facility):
    '''
    Name/Purpose: This function generates a bar graph from a list of objects to show the facilities categories and facilities courts of each Park objects on the list.
    Parameter: A list of Park objects and a string represents the user's requested facility
    Return: None
    Raises/Throws: If the facility is not a string or the parks list is not a list, a Type Error will be raised.
    '''
    if not isinstance(closest_parks, list):
        raise TypeError("The closest parks passed in needs to be a list.")
    if not isinstance(user_facility, str):
        raise TypeError("The facility needs to be a string.")
    park_display_number = FIRST_PARK_DIAPLAY_INDEX
    y_coordinate_range = get_maximum_facilities_count(closest_parks) + CEILING
    plt.figure(figsize=(FIGURE_SIZE_WIDTH, FIGURE_SIZE_HEIGHT))
    for park in closest_parks:
        plt.subplot(GRAPHS_ROW, NUMBER_GRAPH_PER_ROW, park_display_number)
        bar_color = highlight_requested_facility_bar(user_facility, park)
        plt.bar(range(len(park.facilities)), list(park.facilities.values()), color = bar_color, align = "center")
        plt.xticks(range(len(park.facilities)), list(park.facilities.keys()), rotation = LABLE_ANGLE)
        plt.yticks(range(Y_COORDINATE_START_POINT, y_coordinate_range + 1))
        plt.title(park.name)
        plt.xlabel("Park Facilities")
        plt.ylabel("Counts")
        park_display_number += 1
    plt.tight_layout(pad=0.1)
    plt.show()

def get_maximum_facilities_count(closest_parks):
    '''
    Name/Purpose: This function gets the maximum number of the facilities in the list of parks
    Parameter: A list of Park objects
    Return: An integer represents the maximum counts among all the facilities
    Raises/Throws: None
    '''
    maximum_count = 0
    for park in closest_parks:
        for count in park.facilities.values():
            if count > maximum_count:
                maximum_count = count
    return maximum_count

def highlight_requested_facility_bar(user_facility, park):
    '''
    Name/Purpose: This function gets a different color for the bar representing the user's requested facility from other bars in the bar graph
    Parameter: A string represents the user's requested facility and a park object
    Return: A list of strings represent the color of the bars
    Raises/Throws: If the park passed in is not a Park object, a Type Error will be raised.
    '''
    if not isinstance(park, Park):
        raise TypeError("The park passed in needs to be a Park object.")
    bar_color = []
    for facility in park.facilities.keys():
        if facility == user_facility:
            bar_color.append(USER_FACILITY_BAR_COLOR)
        else:
            bar_color.append(OTHER_BAR_COLOR)
    return bar_color

def main():
    try:
        school = download_data("https://opendata.vancouver.ca/explore/dataset/schools/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B")
        park = download_data("https://opendata.vancouver.ca/explore/dataset/parks/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B")
        park_facilities = download_data("https://opendata.vancouver.ca/explore/dataset/parks-facilities/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B")
        school_list = get_school_detail(get_content_row(school))
        school_object_list = get_school_object(school_list)
        park_list = get_park_location(get_content_row(park))
        park_facilities_list = get_park_facilities_detail(get_content_row(park_facilities))
        park_object_list = get_park_object(park_list, park_facilities_list)
        get_user_school_and_facility(school_object_list, park_facilities_list)
        parks_with_requested_facility_list = get_parks_with_facility(global_facility_var, park_object_list)
        user_school_object = get_user_school_object(global_school_var, school_object_list)
        closest_parks = get_list_of_closest_parks_with_facilities(user_school_object, parks_with_requested_facility_list)
        display_closet_parks_with_facilities(user_school_object, closest_parks)
        make_bar_graph_from_objects(closest_parks, global_facility_var)
    except ValueError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
