import sys
import heapq
sys.setrecursionlimit(10000000)
sys.stdin = open('13904_input.txt')
input = sys.stdin.readline

# n의 대표자 찾기
def find(n):
    parent = d_list[n]
    if parent == n:
        return n
    else:
        rep = find(parent)
        d_list[n] = rep
        return rep

if __name__ == '__main__':
    N = int(input().rstrip())
    q = []

    # 각 원소별 대표자 노드 저장
    d_list = [i for i in range(1001)]
    homework = [0] * (1001)

    for _ in range(N):
        d, w = map(int, input().split())
        heapq.heappush(q, [-w, d])

    while q:
        w, d = heapq.heappop(q)
        w = -w

        # d의 대표자 찾기
        rep = find(d)

        if rep == 0:
            continue

        if w > homework[rep]:
            homework[rep] = w
            d_list[rep] = rep - 1
    
    print(sum(homework))