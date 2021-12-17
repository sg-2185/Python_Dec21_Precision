import LMS_new_dec11 as lms

#############################################
# ---------INITIALIZE ALL DATA--------------#
#############################################
# Supply all inputs
l_cname = "M"
l_CreditScore = 400
l_LoanAmount = 15000
l_master_data = lms.get_master_data()
l_check = {}
l_res = None
l_all_cs = []
l_all_loan_amt = []
l_reject = 0
l_total_amount = 0

# Call Business Logic functions
l_check = lms.qualifyCheck(p_master_data=l_master_data, p_CreditScore=l_CreditScore, p_LoanAmount=l_LoanAmount)

if l_check["status"] == "success":
    l_res = lms.calculateLoanDetails(l_master_data, l_cname, l_CreditScore, l_LoanAmount)
    print(l_res)
else:
    print(l_check)

