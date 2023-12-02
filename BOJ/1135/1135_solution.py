import sys
from collections import defaultdict
sys.stdin = open('1135_input.txt')
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    parents = list(map(int, input().split()))

    # dp: 각 노드에서 서브트리로 뉴스를 전파하는 데 걸리는 최소 시간 저장
    min_time = defaultdict(list)
    
    for i in range(N - 1, -1, -1):
        # leaf일 경우
        if not min_time[i]:
            min_time[parents[i]].append(0)
            continue
        
        # 서브트리 중 가장 많은 시간이 걸리는 서브트리부터 뉴스 전파
        min_time_sorted = sorted(min_time[i], reverse=True)
        for j in range(len(min_time_sorted)):
            min_time_sorted[j] += j + 1
        
        min_time[parents[i]].append(max(min_time_sorted))
    
    print(min_time[-1][0])