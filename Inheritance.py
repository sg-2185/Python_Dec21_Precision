class ParentClass():
    Parentvar1 = "parentVariable Value"
    def parentFunction(self):
        print("This is a message from ParentClass.parentFunction")

class ChildClass(ParentClass):
    ChildVar1 = "parentVariable Value"
    def childFunction(self):
        print("This is a message from ChildClass.childFunction")

cObj = ChildClass()

cObj.childFunction()
cObj.parentFunction()





