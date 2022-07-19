input_number = int(input())
cycle = 0
current_number = input_number

while True:
    if current_number < 10:
        sum_digit = current_number
    else:
        sum_digit = int(str(current_number)[0]) + int(str(current_number)[-1])
    
    new_number = int(str(current_number)[-1] + str(sum_digit)[-1])
    cycle += 1
    if input_number == new_number:
        break
    else:
        current_number = new_number

print(cycle)