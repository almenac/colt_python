person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {item[0]:item[1] for item in person}
print(answer)

answer = {k:v for k,v in person}
print(answer)




    