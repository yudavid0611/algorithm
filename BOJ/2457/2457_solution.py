import sys
sys.stdin = open('2457_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
flowers = [list(map(int, input().split())) for _ in range(N)]

# 개화 시기를 기준으로 오름차순 정렬
sort_key = lambda x: (x[0], x[1])
flowers.sort(key=sort_key)

# 개화 시기의 기준점
criteria = [3, 1]

# 개화 시기를 충족하는 꽃 중 지는 시기가 가장 늦은 꽃을 저장
best_flower = flowers[0]

# 조건을 만족할 수 없는 경우
if best_flower[0] > criteria[0] or (best_flower[0] == criteria[0] and best_flower[1] > criteria[1]):
    print(0)

else:
    idx_flower = 1
    answer = 1
    while idx_flower < N:
        while idx_flower < N:
            flower = flowers[idx_flower]
            if flower[0] > criteria[0] or (flower[0] == criteria[0] and flower[1] > criteria[1]):
                break
            
            # 지는 시기가 best flower보다 더 늦을 경우
            if flower[2] > best_flower[2] or (flower[2] == best_flower[2] and flower[3] > best_flower[3]):
                best_flower = flower
            
            idx_flower += 1

        # criteria 업데이트
        criteria[0], criteria[1] = best_flower[2], best_flower[3]
        if best_flower[2] == 12:
            break
        
        # 업데이트한 criteria를 충족 못 할 경우 idx_flower + 1
        if flower[0] > criteria[0] or (flower[0] == criteria[0] and flower[1] > criteria[1]):
            idx_flower += 1

        answer += 1
    
    # 조건을 만족한 경우
    if best_flower[2] == 12:
        print(answer)
    else:
        print(0)