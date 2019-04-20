# names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]

def extract_full_name(dct):
    return list(map(lambda val: "{} {}".format(val["first"], val["last"]), dct))

# def extract_full_name(dct):
#     return list(
#         map(lambda val: f"{val["first"]} {val["last"]}", dct)
#         )

print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']