# Libraries
import backend_functions
import configs
from pysqlitecipher import sqlitewrapper

# Calls top level
def testcases():
    phone_number = "12312311223"
    phone_number2 = "123-123-12"
    testphone = phone_verification(phone_number)
    testphone2 = phone_verification(phone_number2)

    if ( testphone == True):
        print("Phone verification error")
    if ( testphone2 == True):
        print("Phone verification error")

    return 0

#Phone Number Verification
#Check to make sure input is all numbers
#Check to make sure input is correct number of characters (10)
#Input will be a string of characters
#Return a T/F Boolean Value

def phone_verification(phone_number):

    if len(phone_number) == 10:

        if phone_number.isdigit():
            return True
        else:
            print("Make sure the phone number is ALL numbers (no special characters such as - )")
    else:
        print("Make sure the phone number is EXACTLY 10 Numbers.")

    return False

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
        ccounter = 0
        for textfield in checklist:
            if ccounter == listindex:
                if searchtext == textfield:
                    return checklist

            ccounter += 1
    return -1

# Calls main function
if __name__ == '__main__':
    testcases()
