#Contact management system using python
#Author: Sachin Mishra
#This will store contacts of people which include name, phone number, email 
#We will have the option to add ,edit ,delete and view all the contacts 
#Version 1.0
from Filehandler import readFile,writeFile
from editContact import edit
from addContacts import add
from deleteContact import delete
from view import view
from search import search
print("Welcome to CMS ")
lst=readFile()
a=0
while a!=9:
    print("\n\n")
    print("Please choose the desired option")
    print("1/View Contacts")
    print("2/Add Contacts")
    print("3/Delete Contacts")
    print("4/Search Contacts")
    print("5/Edit Contacts")
    print("9/Exit CMS")
    a=int(input("Enter your choise: "))
    print("\n\n")
    match a:
        case 1:
            view(lst)
        case 2:
            lst=add(lst)
        case 3:
            lst=delete(lst)
        case 4:
            search(lst)
        case 5:
            lst=edit(lst)
        case 9:
            print("Closing Program")
        case _:
            print("Invalid option")
writeFile(lst)
