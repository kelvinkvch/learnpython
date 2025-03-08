greeting = 'Hello World'

total = 0
iteration = 0

numbers = [2, 4, 6, 8]

for num in numbers:
    total += num
    iteration += 1
    iteration_num = f'Iteration {iteration} complete'
    print(iteration_num)

print(total)
