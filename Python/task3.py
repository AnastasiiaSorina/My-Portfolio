#A loop that produces a pyramid of asterisks.
#Variant 1 Concatenation

asterisks = "*"

#A loop that adds a new star with each iteration using concatenation.
for triangle in  range(1,6):
    print(asterisks)
    asterisks += "*"


#Variant 2 Slice

#Variable declaration
asterisks = "*****"
counter = 1

for triangle in  range(1,6):
    slice_object = slice(counter)
    print(asterisks[slice_object])
    counter += 1
    
#P.S: I updated task 7 after your review and made some edits.

 

