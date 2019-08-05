'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(arg_list, com, loc, val=None):
    if com == "remove" and loc == "end":
        return arg_list.pop()
    elif com == "remove" and loc == "beginning":
        return arg_list.pop(0)
    elif com == "add" and loc == "beginning":
        arg_list.insert(0, val)
        return arg_list
    elif com == "add" and loc == "end":
        arg_list.append(val)
        return arg_list