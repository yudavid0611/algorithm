tc = int(input())
scores = list(map(int, input().split()))

m = max(scores)

result = 0
for i in scores:
    result += i / m * 100

result = result / tc
print(result)