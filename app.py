#1. Use of AND Operator

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("In-eligible for loan")

#2. Use of AND Operator

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("In-eligible for loan")

#3. Use of NOT Operator

has_high_income = True
has_criminal_record = True

if has_high_income and not has_criminal_record:
    print("Eligible for loan")
else:
    print("In-eligible for loan")
