'''
반례
1
4 3
2 3
3 4
4 4
'''
import sys
from collections import deque
sys.setrecursionlimit(1000000)
sys.stdin = open('9576_input.txt')
input = sys.stdin.readline

# 대표자를 찾는 함수
def find(n):
    parent = books[n]
    if parent == n:
        return parent
    else:
        rep = find(parent)
        return rep
    
T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().split())
    people = []
    for _ in range(M):
        a, b = map(int, input().split())
    
        # 간격
        dist = b - a
        people.append([dist, a, b])
    
    # 간격 기준으로 오름차순 정렬
    people.sort()
    people = deque(people)
    
    books = [i for i in range(N + 1)]
    answer = 0
    while people and answer < N:
        _, a, b = people.popleft()

        book = find(b)
        
        # 책을 나눠줄 수 있을 경우
        if book >= a:
            
            # 대표자 변경
            books[book] = book - 1
            answer += 1
    
    print(answer)