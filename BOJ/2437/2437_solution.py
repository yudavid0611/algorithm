import sys
sys.stdin = open('2437_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
scales = sorted(list(map(int, input().split())))

max_weight = 0
for s in scales:
    if s > max_weight + 1:
        break
    else:
        max_weight += s

print(max_weight + 1)