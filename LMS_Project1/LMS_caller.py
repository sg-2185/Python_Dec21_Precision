import lms_main as lms

# Supply all inputs

l_CustName = "A"
l_CreditScore = 350
l_LoanAmount = 13000
l_master_data = lms.getMasterData()
l_check = {}
l_res = None


# Call Business Logic functions
l_check = lms.qualifyCheck(p_master_data=l_master_data, p_CreditScore=l_CreditScore, p_LoanAmount=l_LoanAmount)

if l_check["status"] == "success":
    l_res = lms.calculateLoanDetails(l_master_data, l_CustName, l_CreditScore, l_LoanAmount)
    print(l_res)
else:
    print(l_check)
