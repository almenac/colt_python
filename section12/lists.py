# numbers = [1, 2, 3, 4, 5]

# for index, num in enumerate(numbers):
#     print(f"Index {index}: {num}")

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

# sounds.append("boo")

# print(sounds)

# Create a list called instructors
# instructors = []
# # Add the following strings to the instructors list 
#     # "Colt"
#     # "Blue"
#     # "Lisa"
# instructors.extend(["Colt", "Blue", "Lisa"])
# # Run the tests to make sure you've done this correctly!
# print(instructors)

# Create a list called instructors

instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
    
instructors.extend(["Colt", "Blue", "Lisa"])

# Remove the last value in the list

instructors.pop()

# Remove the first value in the list

instructors.pop(0)

# Add the string "Done" to the beginning of the list

instructors.insert(0, "Done")

# Run the tests to make sure you've done this correctly!

print(instructors)
