programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from the dictionary 
print(programming_dictionary["Function"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Delete contents of dictionary
programming_dictionary = {}

# Edit content in dictionary
programming_dictionary["Bug"] = "A moth in the computer"

# Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])