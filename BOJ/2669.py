# import sys
# sys.stdin = open('BOJ/input.txt', 'r')

result = 0
squares = []
for i in range(4):
    squares.append(list(map(int, input().split())))

for x in range(100):
    for y in range(100):
        for s in squares:
            # x, y 좌표에 해당하는 네모 칸이 사각형 내에 있는지 확인
            if s[0] <= x < s[2] and s[1] <= y < s[3]:
                result += 1
                break
print(result)