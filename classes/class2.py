class student:
    def input(self):
        name=input("Enter name of the student")
        rollno=int(input("Enter roll no"))
        prn=int(input("Enter prn no"))
        address=(input("Enter address"))
    def display1(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("prn:",self.prn)
        print("address:",self.address)
class cse(student):
    def getmarks(self):
        marks=float(input("Eneter marks"))
    def getsubjects(self):
        subjects=input("Enter Subjects")
    def  display2(self):
        print("marks:",self.marks)
        print("subjects:",self.subjects)
c=cse()
c.input()
c.display1()
c.getmarks()
c.getsubjects()
c.display2()
        

        
