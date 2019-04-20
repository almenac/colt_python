# instructor = {
#     "name": "Colt",
#     "owns_dog": True,
#     "num_courses": 4,
#     "favorite_language": "Python",
#     "is_hilarious": False,
#     44: "my_favorite_number!"
# }

# for k,v in instructor.items():
#     print(f"Key is {k}, value is {v}")

# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]

# # make sure your solution is assigned to the answer variable so the tests can work!
# answer = {list1[i]: list2[i] for i in range(0,len(list1))}

# print(answer)

# person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# # use the person variable in your answer
# answer = {person[i][0]: person[i][1] for i in range(0, len(person))}

# print(answer)

# vowels = "aeiou"

# answer = dict.fromkeys(vowels, 0)

# print(answer)

# answer = {char:0 for char in vowels}

# print(answer)

answer = {k:chr(k) for k in range(65,91)}

print (answer)
