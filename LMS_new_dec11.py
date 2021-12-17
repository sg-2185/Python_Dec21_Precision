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


#############################################
# ---------GET MASTER DATA--------------------#
#############################################
from LMS_main import l_all_cs, l_all_loan_amt


def get_master_data():
    return [
        {"cs_start": 100, "cs_end": 199, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 5, "duration": 65}
        , {"cs_start": 400, "cs_end": 499, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 3.5,
           "duration": 65}
        , {"cs_start": 200, "cs_end": 299, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 4.5,
           "duration": 65}
        ,
        {"cs_start": 300, "cs_end": 399, "loan_amt_start": 10000, "loan_amt_end": 19999, "interest": 4, "duration": 65}
    ]


l_master_data = get_master_data()


##########################################
# -----------END GET MASTER DATA----------#
##########################################

##########################################
# ----------CHECK IF CUSTOMER QUALIFIES---#
##########################################
def qualifyCheck(p_master_data, p_CreditScore, p_LoanAmount):
    for c in p_master_data:
        l_all_cs.append(c["cs_start"])
        l_all_cs.append(c["cs_end"])
        l_all_loan_amt.append(c["loan_amt_start"])
        l_all_loan_amt.append(c["loan_amt_end"])

    if p_CreditScore < min(l_all_cs) or p_CreditScore > max(l_all_cs):
        # print("Credit Score Too Low or Too High")
        return {"status": "rejected"
            , "reason": "Credit Score Too Low or Too High"}
    #
    elif p_LoanAmount < min(l_all_loan_amt) or p_LoanAmount > max(l_all_loan_amt):
        # print("Requested loan amount Too Low or Too High")
        return {"status": "rejected"
            , "reason": "Requested loan amount Too Low or Too High"}
    #
    else:
        return {"status": "success"
            , "reason": "Requested loan amount and Credit Score qualified."}


#############################################
# -----------END CHECK QUALIFY---------------#
#############################################

#############################################
# -----------CALCULATE LOAN AMOUNT-----------#
#############################################
def calculateLoanDetails(p_master_data, p_cust_name, p_CreditScore, p_LoanAmount):
    for c in p_master_data:
        # print(c)
        if c["cs_start"] <= l_CreditScore <= c["cs_end"] and c["loan_amt_start"] <= l_LoanAmount <= c["loan_amt_end"]:
            l_total_amount = l_LoanAmount + (l_LoanAmount / 100) * c["interest"]

        return {"status": "success"
            , "CustomerName": p_cust_name
            , "CreditScore": p_CreditScore
            , "LoanAmount": p_LoanAmount
            , "TotalAmount": l_total_amount
            , "Interest": c["interest"]
            , "Duration": c["duration"]}

    return {"status": "error"
        , "CustomerName": p_cust_name
        , "CreditScore": p_CreditScore
        , "LoanAmount": p_LoanAmount
        , "TotalAmount": 0
        , "Interest": 0
        , "Duration": 0}

############################################
# -------------END CALCULATE LOAN AMOUNT----#
############################################
