def sum_odd_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 != 0:
            total += num
    
    return total

numbers = [x for x in range(1,8)]

print(sum_odd_numbers(numbers))

