# Libraries
from pysqlitecipher import sqlitewrapper
import getpass  # FIXME add a security module
import os
import configs

# Resources
# https://medium.com/@harshnative/encrypting-sqlite-database-in-python-using-pysqlitecipher-module-23b80129fda0

# Checks core functions of library
def testcases():

    # Set variables for run
    database_file_path = configs.test_database_file_path
    table_name = configs.cust_table

    # Data to be added
    col_list = configs.cust_col_list
    insert_list = configs.cust_test_list.copy()
    update_list = configs.cust_test_list.copy()
    new_name = "Jamerson"
    update_list[1] = new_name

    # Delete old and create new database
    if os.path.exists(database_file_path):
        os.remove(database_file_path)

    # Use this to create object for interacting with database
    obj = sqlitewrapper.SqliteCipher(dataBasePath=database_file_path, checkSameThread=False,
                                     password=configs.test_password)

    # Create table for database
    obj.createTable(table_name, col_list, makeSecure=True, commit=True)

    # Add data to data table
    obj.insertIntoTable(table_name, insert_list, commit=True)

    # Retrieve results and check data was imported
    get_col_list, value_list = obj.getDataFromTable(table_name, raiseConversionError=True, omitID=False)

    if not( get_col_list[1:] == configs.check_cust_col_list):
        print("Failed to add table cols")
        return -1

    check_value_list = copy_cut_sublist(value_list)
    if not( check_value_list == insert_list):
        print("Failed to add data row")
        return -1

    # Check update data
    obj.updateInTable(table_name, 0, "lastname", new_name, commit=True, raiseError=True)
    check_col_list, value_list = obj.getDataFromTable(table_name, raiseConversionError=True, omitID=False)

    # Return without first column
    check_value_list = copy_cut_sublist(value_list)
    if not( check_value_list == update_list):
        print("Failed to update data")
        return -1

    # Todo add 2nd user
    obj.insertIntoTable(table_name, configs.second_acct, commit=True)
    check_col_list, value_list = obj.getDataFromTable(table_name, raiseConversionError=True, omitID=False)

    # Check new table

    # Example: Use this to create object for interacting with database
    new_obj = sqlitewrapper.SqliteCipher(dataBasePath=database_file_path, checkSameThread=False,
                                     password=configs.test_password)

    check_col_list, value_list = new_obj.getDataFromTable(table_name, raiseConversionError=True, omitID=False)

    # Todo add user table

    # Todo future function support, not needed for rollout
    # obj.deleteDataInTable(table_name, row_num, commit=True, raiseError=True, updateId=True)
    # obj.changePassword(newPass)

    print("Passed all tests!")
    return 0

# Function for doing actions or calcs
def print_example(x):
    print(f'My favorite number is {x}')    # Example of f-string
    return 0

# todo ask for default user city, state, zip code
def create_customer_database():

    # Initialize variables
    password1 = "123456"
    password2 = "password2"

    # Get info from user
    i = 0
    while (password1 != password2) and i < 10:
        pasword1 = str(input("Enter loyalty database password"))
        pasword2 = str(input("Re-enter password"))
        if pasword1 != password2:
            password = password2
            input ("Here is your loyalty database password: " + password1)
            # print("Do not lose this password!")
        else:
            input("Passwords do not match") # Enter to confirm
        i = i + 1

    # TODO Rename old file
    if os.path.exists(configs.cust_datapath):
        date_time = "2025_05_26"
        os.rename(configs.cust_datapath, configs.cust_datapath+date_time+".bak")
        os.remove(configs.cust_datapath)

    # Create database
    obj = sqlitewrapper.SqliteCipher(dataBasePath=configs.cust_datapath, checkSameThread=False, password=password)

    # Create Table for customers
    obj.createTable(configs.cust_table, configs.cust_col_list, makeSecure=True, commit=True)

    # Add test customer
    obj.insertIntoTable(configs.cust_table, configs.cust_test_list, commit=True)

    # Check test customer
    get_col_list, value_list = obj.getDataFromTable(configs.cust_table, raiseConversionError=True, omitID=False)
    # Return without first column
    test_case_list = copy_cut_sublist(value_list)
    if not (test_case_list == configs.cust_test_list):
        print("Failed to add test user to datatable")
        return -1

    # Create Table for users
    obj.createTable(configs.user_table, configs.user_col_list, makeSecure=True, commit=True)

    # Add admin account
    # TODO Add encoded password here
    obj.insertIntoTable(configs.user_table, configs.user_test_list, commit=True)

    # Check test customer
    get_col_list, value_list = obj.getDataFromTable(configs.user_table, raiseConversionError=True, omitID=False)
    # Return without first column
    test_case_list = copy_cut_sublist(value_list)
    if not (test_case_list == configs.cust_test_list):
        print("Failed to add test user to datatable")
        return -1

    pass

    # Exit if info not valid

    # For multithreading use checkSameThread = True
    #obj = sqlitewrapper.SqliteCipher(dataBasePath=database_file_path, checkSameThread=False, password=password)

def copy_cut_sublist(full_list):
    temp_list = []
    for i in full_list:
        for j in i:
            temp_list.append(j)
        ret_list = temp_list[1:]
        return ret_list

    return -1

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
    testcases()
