#A simple calculator app, "+ - */" with two numbers.
#If you what to enter from the calculation write stop.

#Create a variable for the user's filename. 
file_user = input("Enter file name:\nYou don't need to add the '.txt' at the end*\t")
file_user_calculation = (f"{file_user}.txt")
    #Take data from the user.
while True:
    try:
        first_number = input("\nEnter the first number?\t")
        first_number = int(first_number)
        
    #Checking the entered value first number.
    except ValueError:
        if first_number.lower() ==  "stop":
            print("You are done with the calculator.")
            break
        elif first_number.lower()  ==  "read file":
            user_fail = open(file_user_calculation, 'r')
            print(user_fail.read())
            user_fail.close() 
            break
             
        else:
            print("Please enter correct first number")
            break

    #User enter operator
    operator = input("Enter operator? +  -  *  /\t")

    try:
        second_number = input("Enter the second number?\t")
        second_number = int(second_number)
        
    #Checking the entered value second number.
    except ValueError:
            if second_number.lower()  ==  "stop":
                print("You are done with the calculator.")
                break
            else:
                print("Please enter correct second number")
                break

    #Meetings calculator.
    if (operator == "+"):
            sum = first_number + second_number
            
    elif (operator == "-"):
            sum = first_number - second_number

    elif (operator == "*"):
            sum = first_number * second_number

    elif (operator == "/"):
                
    #Checking divide by zero.
        if first_number == 0:
            print("Oops, you can't divide by zero. Enter the new value, please.") 
            break      
        else :
            sum = first_number / second_number                     
                    
    #Checking if the operator is entered correctly.
    else:
        print("Please enter one of the suggested operations.")  
        break

    #Show result.
    result = (f"\n{first_number} {operator} {second_number} = {sum}")
    print(result) 
        
    # do stuff with file here  
    try:
        
        user_fail = open(file_user_calculation, 'a')
        user_fail.write(result)

    except FileNotFoundError as error:
        print("The file that you are trying to open does not exist")        
    
    finally:
        if user_fail is not None:
            user_fail.close()  

    print("If you want finish, write stop")
    print("if you want to read all of the equations, write 'read file'")
