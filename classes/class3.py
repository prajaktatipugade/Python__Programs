class student:
    def input(self,name,rollno,prn,address):
        self.name=name
        self.rollno=rollno
        self.prn=prn
        self.address=address
    def display1(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("prn:",self.prn)
        print("address:",self.address)
class cse(student):
    def getmarks(self,marks):
        self.marks=marks
    def getsubjects(self,Subject1,Subject2,Subject3,Subject4):
        self.subjects={Subject1,Subject2,Subject3,Subject4}
    def  display2(self):
        print("marks:",self.marks)
        for i in self.subjects:
            print("subjects:",i)
c=cse()
c.input("prajakta",28,123,"kadamwadi")
c.display1()
c.getmarks(89)
c.getsubjects("Science","Maths","English","geography")
c.display2()
