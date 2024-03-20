import os

"""
In this script, you'll create a bot to add some
functionality to Stanford University's Explore Courses 
website using a pre-scraped list of courses and their 
corresponding codes (all stored in `courses.txt`!)
"""

pathname = os.path.dirname(__file__) + "/courses.txt"

# This code splits up the file into a list of courses...
with open(pathname, "r") as file_in:
    courses = {course.split(":")[0]: " ".join(course.split(":")[1:]).strip() for course in file_in.readlines()}

while True:
    # Poll the user to enter an option.
    print("Welcome to the course catalogue!")
    print("Please enter an option to search:")
    print("1 - Search by course number")
    print("2 - Search by course name")
    print("3 - Exit")
    option = input()
    # Implement your code here!