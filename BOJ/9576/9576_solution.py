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
        books[n] = rep
        return rep
    
T = int(input().rstrip())

for _ in range(T):
    N, M = map(int, input().split())
    people = []
    for _ in range(M):
        a, b = map(int, input().split())
        people.append([a, b])
    
    # b 기준 오름차순 정렬
    people.sort(key=lambda x: x[1])
    people = deque(people)
    
    books = [i for i in range(N + 2)]
    answer = 0
    while people and answer < N:
        a, b = people.popleft()

        # 가능한 가장 작은 숫자의 책을 선택
        book = find(a)
        
        # 책을 나눠줄 수 있을 경우
        if book <= b:
            
            # 대표자 변경
            books[book] = book + 1
            answer += 1
    
    print(answer)