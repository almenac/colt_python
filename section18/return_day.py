# def return_day(num):
#     if num == 1:
#         return "Sunday"
#     elif num == 2:
#         return "Monday"
#     elif num == 3:
#         return "Tuesday"
#     elif num == 4:
#         return "Wednesday"
#     elif num == 5:
#         return "Thursday"
#     elif num == 6:
#         return "Friday"
#     elif num == 7:
#         return "Saturday"
#     elif num < 1 or num > 7:
#         return None

def return_day(num):
    weekdays = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    if num > 0 or num < 8:
        return weekdays.get(num)
    return None

print(return_day(3))
print(return_day(15))
print(return_day(-1))



