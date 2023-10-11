# numbers = [1, 2, 3, 4, 5, 99, 2600, 300]

# numbers.reverse()
# print(numbers)



# part 2

# string = "boobie"
# list = []

# for letter in string:
#     list.append(letter)   

# reverse_list = list.reverse()

# print(list)

# new_variable = ""

# new_variable = "".join(list)

# print(new_variable)


#part 3

new_list = ["JCole", "KendrickL", "Drake" ]

new_person = "Jeezy"

if new_person in new_list:
    new_list.remove(new_person)
else:
    new_list.append(new_person)

print(new_list)