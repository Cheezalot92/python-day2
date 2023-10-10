import random 


user_num = int(input("Guess the magic number!"))

magic_number = random.randint(1, 10)
magic_number = 5
while user_num != magic_number:
    if user_num > 10:
        print("YOU'RE OUT OF RANGE!!")
        user_num = int(input("Guess again!"))
    else:
        print("Wrong Answer, try again!")
        user_num = int(input("Guess again!"))
print(f"Congratulations {magic_number} was the magic number")