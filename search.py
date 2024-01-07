from typing import List
from Contacts import Contact
def search(lst: List[Contact]):
    print("How do you want to search")
    print("1/By Name")
    print("2/By Phone")
    opt=int(input("Enter your choice"))
    if opt==1:
        nam=input("Enter the name")
        flag=0
        for i in lst:
            if i.name==nam :
                print(i)
                flag=1
        if flag==0:
            print("The contact doesnot exit")
    if opt==2:
        ph=input("Enter the phone number")
        flag=0
        for i in lst:
            if i.phone==ph :
                print(i)
                flag=1
        if flag==0:
            print("The contact doesnot exit")
    