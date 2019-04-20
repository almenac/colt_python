'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list=[1], com="remove", loc="end", val=1):
    if com.lower() == "remove":
        if loc.lower() == "end":
            return list.pop()        
        return list.pop(0)
    elif com.lower() == "add":
        if loc.lower() == "end":
            list.append(val)
            return list        
        list.insert(0, val)
        return list

# tai

# def list_manipulation(collection, command, location, value=None):
#     if(command == "remove" and location == "end"):
#         return collection.pop()
#     elif(command == "remove" and location == "beginning"):
#         return collection.pop(0)
#     elif(command == "add" and location == "beginning"):
#         collection.insert(0,value)
#         return collection
#     elif(command == "add" and location == "end"):
#         collection.append(value)
#         return collection

# print(list_manipulation([1,2,3], "remove", "end"))
# print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))