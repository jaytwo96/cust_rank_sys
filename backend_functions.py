
# Test cases for functions, manual testing for now
def testcases():
    # Tests for
    print(name_checker("Jimbo"))
    print(name_checker("Steven"))

    return 0

def name_checker(test_name):
    if test_name == "Jimbo":
        return "Bad Name"
    else:
        return f'{test_name} is better than Jimbo'

if __name__ == '__main__':
    testcases()
