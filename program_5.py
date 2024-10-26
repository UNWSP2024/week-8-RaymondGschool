# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
import os

courses: dict[str, str] = {}

def clear_console(): os.system('cls')

def get_course_names() -> None:
    while True:
        clear_console()
        print("Enter ':' to finish")
        key: str = input("Course ID: ")
        if ":" in key: return
        value: str = input("Course name: ")
        if ":" in value: return
        courses.update({key : value})
    
def lookup(prompt: str) -> None:
    print(f"\t\tLooking up '{prompt}'")
    print("-" * 50)
    for key in list(courses.keys()):
        if prompt.lower() in key.lower():
            print(f"Course ID: {key}\t\tCourse name: {courses[key]}")

if __name__ == "__main__":
    get_course_names()

    ID: str = input("Lookup courses with ID: ")
    lookup(prompt=ID)