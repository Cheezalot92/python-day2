# start_number = int(input("Give me an starting number"))
# end_number = int(input("Give me an ending number"))

# while start_number <= end_number:
#     print(start_number)
#     start_number += 1

#bonus question

# start = 1
# stop = 30
# step = 2

# user_input = int(input("Choose your number: "))

# if user_input in range(1, 30, 2):
#     print("Your number is in the range! Good job!")
# else:
#     print("Oops! You chose a number outside the range!)")






#part 2 bonus.

my_string = "We're off to see the wizard, the wonderful wizard of OZ"

counter = 0

while counter < len(my_string):
    counter += 1

    if counter > len(my_string):
        break



    if counter % 2 == 0 and my_string[counter - 1] !=" ":
        
        print(my_string[counter - 1])

