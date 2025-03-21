#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
#Input:         Juan Dela Cruz
#Output: Juan Dela Cruz

# Ask for a full name
print("What is your name?")
name = input("Name: ")

# Remove the spaces from the beginning of the full name 
removed_space = name.lstrip()

# Print result
print("\nOutput:", removed_space)
