# Libraries
import dbsearch

# Calls top level
def testcases():

    file_path = r"C:\Users\jaytw\Documents\Database\Checkcashing.csv"
    listoflistscustomer = [] #initialize variable
    checkcollist = csv_import(file_path, listoflistscustomer)
    phoneindex = dbsearch.get_list_index(checkcollist, "phone")
    custlistindex = dbsearch.lookup_lists_of_lists(listoflistscustomer, "5551234567", phoneindex)

    if not( custlistindex == ['Zuckerberg', 'Mark', 'Meta', '5551234567']):
        print("Phone lookup Failed")
        return -1

    return 0

def csv_import(file_path, listoflistscustomer):
    with open(file_path, 'r') as file:
        i = 0
        for line in file:
            buildlist = []
            buildstring = ""
            for letter in line:
                if letter == ",":
                    buildlist.append(buildstring)
                    buildstring = ""
                elif (letter == "»") or (letter =="ï") or (letter =="¿"): #Skips the first three weird characters from the file import
                    pass

                else:
                    buildstring = buildstring + letter

            buildstring = buildstring.strip()
            buildlist.append(buildstring)

            if i == 0:
                checkcollist = buildlist
            else:
                listoflistscustomer.append(buildlist)

            i = i + 1

    return checkcollist

# Calls main function
if __name__ == '__main__':
    testcases()
