numbers = []

for i in range(10):
    num = int(input(f"Enter a number {i+1}: "))
    numbers.append(num)

unique_numbers = list(set(numbers))

print("Unique numbers are:", unique_numbers)

 