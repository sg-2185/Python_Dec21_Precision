import sys

""""
l_UserInput = input("Enter text and press enter: ")
print("text entered " + l_UserInput)

l_custname = input("Enter Customer name: ")
l_creditscore = input("Enter Customer Credit: ")
l_loanamount = input("Enter Customer Requested Loan Amount: ")

print(l_custname, l_creditscore, l_loanamount)
"""

l_UerInput = ""
terminate_str = ":END"  # Termination string ':END'

while True:
    data = input()
    if data.strip() == terminate_str:
        break
    l_UserInput = l_UserInput + "\n" + data

print(l_UerInput)    


