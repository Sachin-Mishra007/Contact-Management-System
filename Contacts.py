#creating contacts calss with the variables name, phone and email to hold the values
class Contact:
    def __init__(self,name,phone,email):
        self.name=name
        self.phone=phone
        self.email=email
    def __str__(self):
        outputString=self.name+ ","+self.phone+","+self.email
        return outputString