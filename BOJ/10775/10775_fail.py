# 시간초과(반례: P가 10000이고 gi가 모두 10000인 경우)
import sys
sys.stdin = open('10775_input.txt')
input = sys.stdin.readline

G = int(input().rstrip())
P = int(input().rstrip())

gates = [0] * (G + 1)
answer = 0
for _ in range(P):
    now_plane = int(input().rstrip())

    if gates[now_plane] == 0:
        gates[now_plane] = 1
        answer += 1
    
    else:
        idx = now_plane - 1
        while idx > 0 and gates[idx] == 1:
            idx -= 1
        
        if idx > 0:
            gates[idx] = 1
            answer += 1
        
        else:
            break

print(answer)