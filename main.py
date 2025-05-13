# Libraries
import backend_functions

# Global Variables
golden_number = 42

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Calls top level
def main():
    # Call top level functions
    print_example(golden_number)

    # Create class object and use class function
    created_object = Person("Joe", 82)
    created_object.myfunc()

    # Call function from other python file
    name_response = backend_functions.name_checker(created_object.name)
    print(name_response)
    # print(backend_functions.name_checker(created_object.name))

    return 0

# Smaller top level functions or classes are defined here

# Function for doing actions or calcs
def print_example(x):
    print(f'My favorite number is {x}')    # Example of f-string
    return 0

# class for creating objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # Functions that can be called from object
  def myfunc(self):
    print("Hello my name is " + self.name)

# Calls main function
if __name__ == '__main__':
    main()
