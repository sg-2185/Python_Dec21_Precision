class GrandParent():
    X = 50
    def __init__(self):
        print("This is a message from the GrandParent.GrandParentFunction")

class Parent1(GrandParent):
    X = 100
    def __init__(self):
        print("This is a message from the Parent_1.ParentFunction")

class Parent2():
    def __init__(self):
        print("This is a message from the Parent_2.ParentFunction")

class Child1(Parent1, Parent2):
    X = 200
    def __init__(self):
        print("This is Child1, it inherits Parent1 and Parent2")

gcObj = GrandParent()
gcObj = Parent1()
gcObj = Parent2()
gcObj = Child1()



