salt = int(input())

max_5 = salt // 5
final_5 = int()
final_3 = int()

for i in range(max_5, -1, -1):
    remain = salt - 5 * i
    if remain == 0:
        final_5 = max_5
        final_3 = 0
        break
    else:
        if remain % 3 == 0:
            final_5 = i
            final_3 = remain // 3
            break

if (final_5 == 0) and (final_3 == 0):
    print(-1)
else:
    print(final_5+final_3)