import sys
sys.setrecursionlimit(10000000)
sys.stdin = open('10775_input.txt')
input = sys.stdin.readline

G = int(input().rstrip())
P = int(input().rstrip())

gates = [i for i in range(G + 1)]
answer = 0

# 대표자를 찾는 함수
def find(n):
    parent = gates[n]
    if parent == n:
        return n
    else:
        # 대표자 업데이트
        rep = find(parent)
        gates[n] = rep
        return rep

# 도킹할 수 있는 게이트 중 숫자가 가장 큰 게이트에 도킹
for _ in range(P):
    now_plapne = int(input().rstrip())
    rep = find(now_plapne)

    if rep == 0:
        break
    else:
        gates[rep] = rep - 1
        answer += 1
        
print(answer)