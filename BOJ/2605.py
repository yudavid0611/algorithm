import sys
sys.stdin = open('BOJ/input.txt', 'r')

people = int(input())
numbers = list(map(int, input().split()))
result = []
for i in range(people):
    result.insert(i-numbers[i], str(i+1))
result = ' '.join(result)
print(result)