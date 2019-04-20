'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

#define single_letter_count below:

def single_letter_count(arg_string, arg_char):
    s = arg_string.lower()
    c = arg_char.lower()

    return s.count(c)

# tai

# def single_letter_count(string,letter):
#     return string.lower().count(letter.lower())