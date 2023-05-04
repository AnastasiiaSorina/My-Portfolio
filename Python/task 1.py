#Compulsory Task 1
swimming = int(input("How many minutes did you swim? "))
cycling = int(input("How many minutes have you been cycling? "))
running = int(input("How many minutes did you run? "))

total_time = swimming + cycling + running

qualifying_time = "Your award: Provincial Colours"
qualifying_time5 = "Your award: Provincial Half Colours"
qualifying_time10 = "Your award: Provincial Scroll"
qualifying_time_more = "Sorry! You don`t have any award."

if total_time == 100 : award = qualifying_time
elif 100 < total_time <=105 : award = qualifying_time5
elif 105 < total_time <=110 : award = qualifying_time10
elif total_time > 110 : award = qualifying_time_more
else : award = "Try again!"

print(f"\nYour total time taken to complete the triathlon {total_time} minutes. \n{award}")

