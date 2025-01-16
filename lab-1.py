YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
END = '\u001b[0m'

strip_height = 4

flag_width = 30

for _ in range(strip_height):
    print(YELLOW + ' ' * flag_width + END)

for _ in range(strip_height):
    print(GREEN + ' ' * flag_width + END)

for _ in range(strip_height):
    print(RED + ' ' * flag_width + END)

plot_list = [[0 for i in range(10)] for i in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = abs(i)

step = round(abs(result[0] - result[9]) / 9, 2)
print(step)

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

for i in range(10):
    #print(plot_list[i])
    pass

with open('sequence.txt', 'r') as file:
    numbers = [float(line.strip()) for line in file]

even_positions = numbers[::2]  
odd_positions = numbers[1::2]  

average_even = sum(abs(x) for x in even_positions) / len(even_positions)
average_odd = sum(abs(x) for x in odd_positions) / len(odd_positions)

total = average_even + average_odd
percentage_even = (average_even / total) * 100
percentage_odd = (average_odd / total) * 100

print(f"Среднее по модулю (чётные позиции): {average_even:.2f}")
print(f"Среднее по модулю (нечётные позиции): {average_odd:.2f}")
print(f"Процентное соотношение (чётные): {percentage_even:.2f}%")
print(f"Процентное соотношение (нечётные): {percentage_odd:.2f}%")

def draw_bar_chart(percentage_even, percentage_odd):
    bar_length = 50  
    even_bar = '#' * int((percentage_even / 100) * bar_length)
    odd_bar = '#' * int((percentage_odd / 100) * bar_length)
    print("\nДиаграмма процентного соотношения:")
    print(f"Чётные позиции: [{even_bar}] {percentage_even:.2f}%")
    print(f"Нечётные позиции: [{odd_bar}] {percentage_odd:.2f}%")

draw_bar_chart(percentage_even, percentage_odd)




