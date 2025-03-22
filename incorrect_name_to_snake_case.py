# Ask for a full nams
print("What is you name?")
name = input("Name: ")

# Correct the incorrect casing of the name and convert into snake case
snakecase_name = name.lower().replace(" ", "_")

# Print the result
print("\nOutput:", snakecase_name)
