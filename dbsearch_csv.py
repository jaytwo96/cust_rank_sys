# Libraries
import backend_functions
import configs
from pysqlitecipher import sqlitewrapper

# Calls top level
def testcases():
    # Set variables for run
    database_file_path = configs.test_database_file_path
    table_name = configs.cust_table

    new_obj = sqlitewrapper.SqliteCipher(dataBasePath=database_file_path, checkSameThread=False,
                                     password=configs.test_password)

    check_col_list, value_list = new_obj.getDataFromTable(table_name, raiseConversionError=True, omitID=True)
    #check_value_list = copy_cut_sublist(value_list)
    phoneindex = get_list_index(check_col_list, "phone")
    loyaltyindex = get_list_index(check_col_list, "loyaltynum")
    custlistindex = lookup_lists_of_lists(value_list, "5557654321", phoneindex)
    loyaltylistindex = lookup_lists_of_lists(value_list, "12345678", loyaltyindex)
    #Lookup loyalty number
    #Handle no number found
    #Todo search loyalty number or phone number within list of lists

    file_path = r"C:\Users\jaytw\Documents\Database\Checkcashing.csv"
    listoflistscustomer = []
    checkcollist = []


    csv_import(file_path, listoflistscustomer, checkcollist)

    #'5187955229,Josh,170 George St Green Island New York 12183\n'
    #strip gets rid of \n
    #Figure out how to separate one string into a list.
    #Create a list of lists for value_list

    if not( custlistindex == configs.second_acct):
        print("Phone lookup Failed")
        return -1

    if not( loyaltylistindex == configs.first_acct):
        print("Loyalty lookup Failed")
        return -1

    return 0

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

def csv_import(file_path, listoflistscustomer, checkcollist):
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            print(line.strip())
            buildlist = []
            buildstring = ""
            for letter in line:
                if letter == ",":
                    buildlist.append(buildstring)
                    buildstring = ""
                elif (letter == "»") or (letter =="ï") or (letter =="¿"): #Skips the first three weird characters from the file imnport
                    pass

                else:
                    buildstring = buildstring + letter

            buildstring = buildstring.strip()
            buildlist.append(buildstring)
            print (buildstring)

            if i == 0:
                checkcollist.append(buildlist)
            else:
                listoflistscustomer.append(buildlist)

            i = i + 1

# Calls main function
if __name__ == '__main__':
    testcases()
