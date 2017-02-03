import re
import os

text_file_string = ""

#Find all ten digit mobile numbers in the string named-> text_file_string
def find_numbers(text_string):
    phoneNumRegex = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
    # Matched object
    print("\nHere we are printing all occourances of the 10 digit number \n")
    mobile_no_list=phoneNumRegex.findall(text_string)
    for no in mobile_no_list:
        print(no)


# traverse root directory, and list directories as dirs and files as files
def traverse_directory():
    global text_file_string
    message ='''Please enter directoty in format like -  C:\\Users\\TestCase\\ ''' 
    print (message)
    directory_string = input("Enter directory\n")
    root = directory_string
    if root == "":
        print ("Invalid Directory Entered")
    else:        
        for item in os.listdir(root):
            if os.path.isfile(os.path.join(root, item)):
                file_path = root + item
                print ("File in path -\t" + file_path + " is parsed")
                file_value = open(file_path)
                text_file_string += " " + file_value.read()
        find_numbers(text_file_string)



traverse_directory()   


