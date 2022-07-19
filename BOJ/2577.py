multiplied = 1
for i in range(3):
    multiplied *= int(input())
multiplied = str(multiplied)
for i in range(10):
    print(multiplied.count(f'{i}'))