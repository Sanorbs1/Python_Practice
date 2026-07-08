def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)
# Output: 1, 2, 3, 4, 5

# Or manually:
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# List comprehension (stores all in memory)
squares_list = [x**2 for x in range(1000000)]

# Generator expression (one at a time)
squares_gen = (x**2 for x in range(1000000))

for square in squares_gen:
    print(square)