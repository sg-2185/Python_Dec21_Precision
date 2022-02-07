"""""
from test import Test as t1

Obj1 = t1()
Obj1.num1 = 100
Obj1.num2 = 200

Obj2 = t1()
Obj2.num1 = 1000
Obj2.num2 = 2000

print(Obj1.__sizeof__() + Obj2.__sizeof__())
"""""


class Tinitiate:
    # CLASS VARIABLES / ATTRIBUTES
    # a class Variable
    ti_var = 100
    # a class list
    ti_list = ["a", "b", "c"]
    # a class tuple
    ti_tuple = ("x", "y", "z")
    # a class dictionary
    ti_dictionary = {"1": "A", "2": "b", "3": "c"}

    # CLASS FUNCTION
    def ti_function(self):
        "This is a class function"
        print("This is a message from the TINITIATE Class ti_function")

ti_object = Tinitiate()
print(ti_object.ti_var)

t_object = Tinitiate()
t_object.ti_function()

print(Tinitiate.__doc__)
print(Tinitiate.__name__)
print(Tinitiate.__module__)
print(Tinitiate.__bases__)


