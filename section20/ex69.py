def interleave(str1, str2):
    str_list = list(zip(str1, str2))
    str_list = ["".join(x) for x in str_list]
    return "".join(str_list)

print(interleave("hi", "ho"))
