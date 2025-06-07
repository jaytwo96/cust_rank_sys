# Libraries
from enum import Enum

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

# Test only variables
test_password = "123456"
test_database_file_path = "test.db"

# Customer List
cust_col_list = [
        ["firstname", DBtype.dbText],
        ["lastname", DBtype.dbText],
        ["address", DBtype.dbText],
        ["lastcompany", DBtype.dbText],
        ["phone", DBtype.dbText],
        ["loyaltynum", DBtype.dbText],
    ]
check_cust_col_list = ['firstname', 'lastname', 'address', 'lastcompany', 'phone', 'loyaltynum']

cust_test_list = ["John", "Appleseed", "123 Main St", "Good Business", "5551234567", "12345678" ]
second_acct = ["Jane", "Doe", "789 6th St", "Better Business", "5557654321", "87654321" ]

# User List
user_col_list = [
        ["username", DBtype.dbText],
        ["password_sha", DBtype.dbText],
        ["position", DBtype.dbText],
    ]

user_test_list = ["admin", "Server password", POStype.posAdmin]

# Resources
# https://medium.com/@harshnative/encrypting-sqlite-database-in-python-using-pysqlitecipher-module-23b80129fda0
