# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

""""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
"""""

""""
variable1 = 4          # Integer
print("variable1 reassigned value: ", variable1)
"""

"""""
l_UserInput = ""
terminate_str = ":END"  # Termination string ':END'

while True:
    data = input()
    if data.strip() == terminate_str:
        break
    l_UserInput += "%s\n" % data

print(l_UserInput)


try:
    raise ti_exception_1
    a = 1
    b = 3
except ti_exception_1:
    print("This is a user defined exception 1 Handler")
except ti_exception_1:
    print("This is a user defined exception 1 Handler")



class too_much_bonus(Exception):pass

sal =
bonus =

try:
    if bonus > (sal/2):
        raise too_much_bonus
except too_much_bonus:
    print("Hey you are getting too much bonus")
else:
    print("Hey your bonus is in right amount")

"""

import os
import subprocess

OScommand = "echo Tinitiate.com"
os.system(OScommand)
subprocess.call(['echo','Hello Tinitiate'], shell=True)
(SDOut,SDErr) = subprocess.Popen( ['echo','Hello World!']
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,universal_newlines=True
                                 ,shell=True).communicate()

print(SDOut)
print(SDErr)












# See PyCharm help at https://www.jetbrains.com/help/pycharm/

