import Contacts as c
import addContacts as a
import deleteContact as d
import editContact as e
import Filehandler as f
#c1=c.Contact("Sachin","7488302853","mishra@gmail.com")
#c2=c.Contact("Renuka","8918507354","renu@gmail.com")
#lst=[c1,c2]
#lst=a.add(lst)
#for i in lst:
#    print(i)
#lst=d.delete(lst)
#e.edit(lst)
lst=f.readFile()
#lst=d.delete(lst)
#lst=f.writeFile(lst)
for i in lst:
    a=str(i)
    print(a)
