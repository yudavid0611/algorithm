n = int(input())
count = 1
last_number = 1
while True:
    if n <= last_number:
        break
    count += 1
    last_number += count*1 + (count-1)*4 + (count-2)*1
print(count)