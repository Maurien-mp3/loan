# Get user to input for  monthly salary and loan amount
def check_loan_eligibility():
    try:
        monthly_salary = float(input("Enter your monthly salary: "))
        loan_amount = float(input("Enter the loan amount you are requesting: "))
    except ValueError:
        print("Please enter a valid number for salary and loan amount.")
        return 
    
    # Check if user is eligble for loan
    if monthly_salary < 30000:
        print("You are not eligible to loan because your salary is less than 30,000. ")
        return
    
    max_loan_amount = monthly_salary * 10
    if loan_amount > max_loan_amount:
        print(f"You are not eligible for a a loan because the requested amount exceeds 10 times your monthly salary. ")
    else:
        print("You are eligible for the loan!")

    # Calculate the total amount with interest
    try:
        repayment_months = int(input("Enter the number of months you want to pay off the loan: "))
    except ValueError:
        print("Please enter a valid number for months.")
        return
    
    # Calculate the loan with 10% interest
    total_amount_with_interest = loan_amount * 1.1
    monthly_payment = total_amount_with_interest / repayment_months 

    print(f"Loan Approved! Total amount with 10% interest: {total_amount_with_interest:.2f}")
    print(f"Your monthly payment {repayment_months} months will be: {monthly_payment:.2f}")

# C
check_loan_eligibility()


















