# Libraries
import backend_functions
import configs
from pysqlitecipher import sqlitewrapper


# Global Variables
golden_number = 42

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Calls top level
def main():
    # Set variables for run
    database_file_path = configs.test_database_file_path
    table_name = configs.cust_table

    new_obj = sqlitewrapper.SqliteCipher(dataBasePath=database_file_path, checkSameThread=False,
                                     password=configs.test_password)

    check_col_list, value_list = new_obj.getDataFromTable(table_name, raiseConversionError=True, omitID=False)
    #check_value_list = copy_cut_sublist(value_list)
    phoneindex = get_list_index(check_col_list, "phone")
    loyaltyindex = get_list_index(check_col_list, "loyaltynum")
    custlistindex = lookup_lists_of_lists(value_list, "5557654321", phoneindex)

    #Todo search loyalty number or phone number within list of lists


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

def copy_cut_sublist(full_list):
    temp_list = []
    for i in full_list:
        for j in i:
            temp_list.append(j)
        ret_list = temp_list[1:]
        return ret_list

    return -1

def get_list_index(full_list, searchtext):
    i = 0
    for textfield in full_list:
        if textfield == searchtext:
            return i

        i += 1


    return -1

#Output: customer list information
#Input example:check val list, "555-555-5555", phoneindex (5)
def lookup_lists_of_lists(full_list, searchtext, listindex):
    for checklist in full_list:
        for textfield in checklist:
            #add column counter
            #if textfield == searchtext
            #return checklist
            pass #temp_list.append(j)

        #ret_list = temp_list[1:]
        #return ret_list

    return -1


# Calls main function
if __name__ == '__main__':
    main()
