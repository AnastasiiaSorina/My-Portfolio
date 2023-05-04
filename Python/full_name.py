#Compulsory Task 1
full_name = input("Enter your name ")
check_full_name = len(full_name)

if check_full_name < 4 and check_full_name != 0:
    print("You entered less than 4 characters. Please make sure you Enter your first and last name.")    
elif check_full_name == 0:
        print("You have entered an invalid value. Try again")
else:
     if check_full_name < 25:
        print("Thank you for providing your name.")
     else:
        print("You have entered more than 25 characters. Please make sure that you have only entered your full name.") 
