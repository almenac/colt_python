'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(arg_list):
    list_len = len(arg_list)
    if list_len > 0:
        return arg_list[list_len -1]
    return None

# tai

# def last_element(l):
#     if l:
#         return l[-1]
#     return None