def generate_evens():
    evens = [num for num in range(1,50) if num % 2 == 0]
    return evens

even_list = generate_evens()

print(even_list)