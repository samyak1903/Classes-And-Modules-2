#Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.
class Cop:
    def __init__(self):
        self.name="Ethan"
        self.age=28
        self.workexp=5
        self.desig="IMF Agent"
    def addDetails(self,name,age,workexp,desig):
        self.name=name
        self.age=age
        self.workexp=workexp
        self.desig=desig
    def display(self):
        print("Secret Agent Details: ")
        print("Name: {}, Age: {}, Work Experience: {}, Designation: {}".\
              format(self.name,self.age,self.workexp,self.desig))
class Mission(Cop):
    mission_details="Recover Stolen Files"
    def add_mission_details(self):
        print("Mission Details= ",self.mission_details)
m=Mission()
name=input("Enter the name of cop:")
age=int(input("Enter age of cop:"))
workexp=int(input("Enter the work experience:"))
desig=input("Enter designation:")
m.addDetails(name,age,workexp,desig)
m.display()
m.add_mission_details()
