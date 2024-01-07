#module to delete a contact
import Contacts as c
from typing import List
def delete(lst :List[c.Contact]):
    print("****For Searching to delete choose the option****")
    print("1/Search using phone number")
    print("2/Search using name")
    print("3/You dont want to continue")
    opt=int(input("Enter your choice"))
    if opt==1:
        ph=input("EMter the number which you want to search")
        flag1=-1
        for i in lst:
            if(i.phone==ph):
                flag1=lst.index(i)
                break
        if(flag1==-1):
            print("Sorry couldnot find the phone number")
            
        else:
            lst.pop(flag1)
            print(ph," deleted successfully ")
    elif opt==2:
        nam=input("ENter the name which you want to search")
        flag2=-1
        for i in lst:
            if(i.name==nam):
                flag2=lst.index(i)
                break
        if(flag2==-1):
            print("Sorry cannot find the name in contacts")
            
        else:
            lst.pop(flag2)
            print(nam," deleted successfully")
    else:
        print("Invalid option entered , please enter a valid option") 
    return lst