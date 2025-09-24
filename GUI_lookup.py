# Libraries
import backend_functions
import configs
from pysqlitecipher import sqlitewrapper
import tkinter as tk

# Calls top level
def testcases():
    # Create the main window (root widget)



    root = tk.Tk()
    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Submit", command=get_input(entry))
    button.pack()

    root.mainloop()

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

def get_input(entry):
    user_text = entry.get()
    print(f"User entered: {user_text}")


def name_verification(name_str):

    if (len(name_str) < configs.name_char_limit) or (len(name_str) > 1):
        for char in name_str:
            if not (char.isalpha()):
                if char == "-" or char == "'":
                    pass
                else:
                    print("Make sure the name DOES NOT contain any special characters.")
                    return False
        return True
    else:
        print(f"Make sure the name is between 1 and {configs.name_char_limit} characters")

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