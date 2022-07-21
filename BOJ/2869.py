info = list(map(int, input().split()))
now = 0
days = 0

threshold = info[2] - info[0]
step = info[0] - info[1]
days += threshold // step
now += days * step

while True:
    days += 1
    # daytime
    now += info[0]
    if now >= info[2]:
        break
    # night
    now -= info[1]
    if now < 0:
        now = 0

print(days)