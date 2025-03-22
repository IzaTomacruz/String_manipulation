# Ask for a full name
print("What is you name?")
name = input("Name: ")

# Correct the incorrect casing of the name and onvert into pascal case
pascal_name = name.title().replace(" ", "")

# Print the result
print("\nOutput:", pascal_name)
