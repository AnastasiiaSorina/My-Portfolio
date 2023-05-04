#The program calculates the average of the numbers entered excluding the -1.

#Declaration of variables for correct operation.
user_number = 0
sum = 0
counter = 0 


while True:
    user_number = int(input("Enter a number?\t"))

#Stop the loop and display the result if the user entered -1.   
    if user_number == -1:
        average = sum / counter
        print(f"\nThe average is {average}")
        break
    
#Calculating the average value for other cases.
    else:
        sum += user_number
        counter += 1
