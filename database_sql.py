# Libraries
import backend_functions
from pysqlitecipher import sqlitewrapper
from enum import Enum
import getpass
import os

# Set enum
class DBtype(Enum):
    dbText = "TEXT" # text / strings
    dbReal = "REAL" # float numbers
    dbInt  = "INT"  # Integer and cash pricing
    dbJSON = "JSON" # JSON Strings LIST — for python list type
    dbBlob = "BLOB" # Binary data

class POStype(Enum):
    posAdmin = "Admin"      # Can reset user passwords and backup data
    posManager = "Manager"  # Can edit customer data, generate reports
    posCashier = "Cashier"  # Can enroll and lookup customers

# make the object

# TODO Move these to global python file
# Global Variables
cust_datapath = "loyalty.db"
cust_table    = "customer_table"
user_table    = "user_table"

# Customer List
cust_col_list = [
        ["rollno", "INT"],
        ["name", DBtype.dbText],
    ]

cust_test_list = [1, "John Appleseed"]

# User List
user_col_list = [
        ["username", DBtype.dbText],
        ["password_sha", DBtype.dbText],
        ["position", DBtype.dbText],
    ]

user_test_list = ["admin", "Server password", POStype.posAdmin]

# Resources
# https://medium.com/@harshnative/encrypting-sqlite-database-in-python-using-pysqlitecipher-module-23b80129fda0

# Checks core functions of library
def testcases():

    # Set variables for run
    password = "123456"
    database_file_path = "test.db"
    table_name = "lookupTable"

    # Data to be added
    col_list = [
        ["rollno", "INT"],
        ["name", DBtype.dbText],
    ]

    check_col_list = ['ID', 'rollno', 'name']
    insert_list = [1, "john"]
    new_name = "jacob"
    update_list = [1, new_name]

    # Delete old and create new database
    if os.path.exists(database_file_path):
        os.remove(database_file_path)
    obj = sqlitewrapper.SqliteCipher(dataBasePath=database_file_path, checkSameThread=False, password=password)

    # Create table for Database
    obj.createTable(table_name, col_list, makeSecure=True, commit=True)

    # Add data to data table
    obj.insertIntoTable(table_name, insert_list, commit=True)

    # Retrieve results and check data was imported
    get_col_list, value_list = obj.getDataFromTable(table_name, raiseConversionError=True, omitID=False)

    if not( get_col_list == check_col_list):
        print("Failed to add table cols")
        return -1

    insert_list = [[0, 1, 'john']]
    if not( value_list == insert_list):
        print("Failed to add data row")
        return -1

    # Check update data
    obj.updateInTable(table_name, 0, "name", new_name, commit=True, raiseError=True)
    check_col_list, value_list = obj.getDataFromTable(table_name, raiseConversionError=True, omitID=False)

    # Return without first column
    some_val = copy_cut_sublist(value_list)
    if not( some_val == update_list):
        print("Failed to update data")
        return -1

    # obj.deleteDataInTable(table_name, row_num, commit=True, raiseError=True, updateId=True)

    # obj.updateInTable(tableName , iDValue , colName , colValue , commit = True , raiseError = True)
    # obj.changePassword(newPass)

    print("Passed all tests!")
    return 0

# Function for doing actions or calcs
def print_example(x):
    print(f'My favorite number is {x}')    # Example of f-string
    return 0

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
    if os.path.exists(cust_datapath):
        date_time = "2025_05_26"
        os.rename(cust_datapath, cust_datapath+date_time+".bak")
        os.remove(cust_datapath)

    # Create database
    obj = sqlitewrapper.SqliteCipher(dataBasePath=cust_datapath, checkSameThread=False, password=password)

    # Create Table for customers
    obj.createTable(cust_table, cust_col_list, makeSecure=True, commit=True)

    # Add test customer
    obj.insertIntoTable(cust_table, cust_test_list, commit=True)

    # Check test customer
    get_col_list, value_list = obj.getDataFromTable(cust_table, raiseConversionError=True, omitID=False)
    # Return without first column
    test_case_list = copy_cut_sublist(value_list)
    if not (test_case_list == cust_test_list):
        print("Failed to add test user to datatable")
        return -1

    # Create Table for users
    obj.createTable(user_table, user_col_list, makeSecure=True, commit=True)

    # Add admin account
    # TODO Add encoded password here
    obj.insertIntoTable(user_table, user_test_list, commit=True)

    # Check test customer
    get_col_list, value_list = obj.getDataFromTable(user_table, raiseConversionError=True, omitID=False)
    # Return without first column
    test_case_list = copy_cut_sublist(value_list)
    if not (test_case_list == cust_test_list):
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
