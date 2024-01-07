#Module to handle file input and output
from Contacts import Contact as c
from typing import List
import csv
def readFile():
    lst=[]
    f=open("contacts.csv","r")
    reader=csv.DictReader(f)
    for i in reader:
        name=i['Name']
        phone=i['Phone']
        email=i['Email']
        c1=c(name,phone,email)
        lst.append(c1)
    return lst
def writeFile(lst :List[c]):
    f=open("contacts.csv","w")
    header="Name,Phone,Email"
    f.write(header+"\n")
    for i in lst:
        ct=str(i)
        f.write(ct+"\n")