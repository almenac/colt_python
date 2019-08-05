'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(el_list):
    if len(el_list) != 0:
        return el_list[-1]
    return None

print(last_element([1,2,3]))
print(last_element([]))