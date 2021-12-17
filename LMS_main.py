"""
Super Loan Management System
CustName    = "A"
CreditScore = 355
LoanAmount  = 23500

Status= Approve/ Rejected
Reason
Interest = %
Duration = 72
TotalAmount = LoanAmount + (LoanAmount/100)*Interest



CS_Start  CS_End    LoanAmtStart  LoanAmtEnd  Interest  Duration
100       199       10000         19999       5         65
200       299       10000         19999       4.5       65
300       399       10000         19999       4         65
400       499       10000         19999       3.5       65

100 + (100/100)*5 = 105

Inputs
    Business rules (Engine)
        Input Data
        LookUp Data / Master Data
        Meta Data
        Transactional Data
Output
"""

l_CustName = "A"
l_CreditScore = 350
l_LoanAmount = 1300

"""

"""
c_master_data = [
    {"cs_start": 100, "cs_end": 199, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 5, "duration": 65}
    , {"cs_start": 400, "cs_end": 499, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 3.5, "duration": 65}
    , {"cs_start": 200, "cs_end": 299, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 4.5, "duration": 65}
    , {"cs_start": 300, "cs_end": 399, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 4, "duration": 65}
]

l_all_cs = []
l_all_loan_amt = []
l_reject = 0


for c in c_master_data:
    l_all_cs.append(c["cs_start"])
    l_all_cs.append(c["cs_end"])
    l_all_loan_amt.append(c["loan_amt_start"])
    l_all_loan_amt.append(c["loan_amt_end"])
""
if l_CreditScore < min(l_all_cs) or l_CreditScore > max(l_all_cs):
    print("Credit Score Too Low or Too High")
    l_reject = 1
if l_LoanAmount < min(l_all_loan_amt) or l_LoanAmount > max(l_all_loan_amt):
    print("Requested loan amount Too Low or Too High")
    l_reject = 1
"""
"""
# print(min(newList))  # OUTPUT: 1
# print(max(newList))  # OUTPUT: 5

# Business Rules Engine
# TotalAmount = LoanAmount + (LoanAmount/100)*Interest


if l_reject == 0:
    for c in c_master_data:
        # print(c)
        if l_CreditScore >= c["cs_start"] and l_CreditScore <= c["cs_end"] and l_LoanAmount >= c[
            "loan_amt_start"] and l_LoanAmount <= c["loan_amt_end"]:
            print(c["interest"])
            print(c["duration"])

            TotalAmout = l_LoanAmount + (l_LoanAmount / 100) * c["interest"]
            print(TotalAmout)


"""
Interest = %
Duration = 72
TotalAmount = LoanAmount + (LoanAmount/100)*Interest
"""

