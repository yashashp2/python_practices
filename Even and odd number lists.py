#Even and odd number lists

number_list = input("Enter numbers separated by a single space: ").split() #split is used to put the numbers entered by a user into a list
even_list = []
odd_list =[] #creating two empty list to separate and store even and odd numbers
print(number_list) #for testing
for number in number_list: #traverse through all the elements of the list
    if int(number) % 2 == 0: #check if a number is even
        even_list.append(number) #inserting even numbers at the end of the even list
    else:
        odd_list.append(number) #inserting odd numbers at the end of the odd list

print(f"Original list :{number_list}")
print(f"Even numbers: {even_list}")
print(f"Odd numbers: {odd_list}")