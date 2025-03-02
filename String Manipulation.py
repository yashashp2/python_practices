# String Manipulation
strings = input("Enter a sentence:\n")

upper_case_string = strings.upper() #method to make a string upper case
lower_case_string = strings.lower() #method to make a string upper case
without_spaces = strings.strip() #method to delete leading and trailing spaces
replaced_string = strings.replace(" ","_") #method to replace specified charater with an other character
print('Uppercase string: '+ upper_case_string)
print('Lowercase string: '+lower_case_string)
print('Spaces replaced with underscore: '+replaced_string)
print('Leading and trailing spaces deleted: '+without_spaces)