numbers = [1, 2, 3, 4, 5]
square_numbers = []

# for loop to square each elements
for num in numbers:
    square_numbers.append(num * num)
    
print(square_numbers)

# Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]

# create a new list using list comprehension
square_numbers = [num * num for num in numbers]

print(square_numbers)

# Output: [1, 4, 9, 16, 25]