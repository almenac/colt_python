def interleave(str1, str2):
    return "".join(["".join(tup) for tup in list(zip(str1, str2))])

print(interleave("hi", "no"))