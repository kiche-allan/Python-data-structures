has_high_income = True

has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

    # AND: - ALL CONDITIONS MUST BE True
    # OR: - ATLEAST ONE CONDITION MUST BE TRUE

has_good_character = True
has_good_behavior = True

if has_good_character and not has_good_behavior:
    print('Should be recruited')