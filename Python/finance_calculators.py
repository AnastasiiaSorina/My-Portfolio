import math

investment = "\ninvestment" "\t- to calculate the amount of interest you'll earn on your investment."
bond = "\nbond" "\t\t- to calculate the amount you'll have to pay on a home loan."
print(investment, bond)
user_decision = (input("\nEnter either 'investment' or 'bond' from the menu above to proceed: \t")).lower()

if user_decision == "investment" :  
    user_money = int(input("\nHow much money do you want to deposit?\t"))
    user_rate = int(input("\nYour interest rate?\t"))
    years = int(input("\nFor how many years do you plan to invest?\t"))
    interest = (input("\nDo you want 'simple' or 'compound' interest?\t")).lower()

    #Percentage calculation
    rate = user_rate / 100
    simple_interest = user_money * (1 + rate * years)
    compound_interest = user_money * math.pow((1 + rate), years)

    if interest == "simple" :  
        print(f"\nThe amount of interest {simple_interest - user_money}")
    elif interest == "compound" :
        print(f"\nThe amount of interest {compound_interest - user_money}")
    else :  
        print("\nThe answer was entered incorrectly, please try again.")

elif user_decision == "bond" :  
    house_price = input("\nWhat is the present value of the house\t")
    user_rate = input("\nYour interest rate?\t")
    months = input("\nHow many months do you plan to pay off the bond?\t")
    
    #Calculation bond repayment
    i = int((user_rate / 100) / 12)
    result = round((i * house_price)/(1 - (1 + i)**(-months))) 
    print(f"\nYour monthly fee is {result}.")

else :
    print("\nThe answer was entered incorrectly, please try again.")