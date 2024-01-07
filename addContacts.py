#module to add a contact
import Contacts
from typing import List
def add(lst: List[Contacts.Contact]):
    name=input("please enter name")
    phone=input("please enter phone number")
    email=input("please enter email id")
    c1=Contacts.Contact(name,phone,email)
    lst.append(c1)
    return lst
