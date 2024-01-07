#module to edit contact
from typing import List
from Contacts import Contact
def edit(lst :List[Contact]):
    nam=input("Enter the name which you want to edit")
    flag1=-1
    for i in lst:
        if(i.name==nam):
            flag1=lst.index(i)
            break
    if(flag1==-1):
        print("The contact doesnot exist")
    else:
        print("Contact details")
        print(lst[flag1])
        print("CHoose the option that you want to edit")
        print("1/Name")
        print("2/Phone")
        print("3/Email")
        opt=int(input("Option Please: "))
        match opt:
            case 1:
                nam=input("ENter the new name")
                lst[flag1].name=nam
            case 2:
                ph=input("Enter new number")
                lst[flag1].phone=ph
            case 3:
                eml=input("Enter new email")
                lst[flag1].email=eml
            case _:
                print("Please enter a valid option")
    return lst    
