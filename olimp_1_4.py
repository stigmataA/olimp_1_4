N = int(input(f'Количество наборов команд: '))
M = int(input(f'Требуемое количество команд с манипулятором: '))

if M == 0:
    print(N)
    exit()

if M > 9:
    print(0)
    exit()

manipulator_digits = {0, 4, 8}

result_counter = 0

for i in range(N):
    number = int(input(f'Номер блока команд: '))
    count = 0

    if number == 0:
        digits = [0]
    else:
        digits = []
        temp_number = number
        while temp_number > 0:
            digit = temp_number % 12
            if digit in manipulator_digits:
                count += 1
            temp_number = temp_number // 12

    if count >= M:
        result_counter += 1

print(result_counter)
