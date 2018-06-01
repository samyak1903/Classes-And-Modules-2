#Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    def animal_attribute(self):
        print("Base Class Animal")
class Tiger(Animal):
    def tiger_attribute(self):
        print("Child Class Tiger")
t=Tiger()
t.animal_attribute()
t.tiger_attribute()
