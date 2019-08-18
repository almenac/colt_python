names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]


def extract_full_name(dicts):
    return list(
        map(
            lambda val: "{} {}".format(val["first"], val["last"]),
            dicts
            )
        )
    

print(extract_full_name(names))