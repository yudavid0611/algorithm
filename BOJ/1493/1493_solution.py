import sys
sys.stdin = open('1493_input.txt')
input = sys.stdin.readline

L, W, H = map(int, input().split())

# 큐브 개수
n_cubes = int(input().rstrip())

# 큐브
cubes = [list(map(int, input().split())) for _ in range(n_cubes)]
cubes.sort(reverse=True)

# 박스의 부피
box_volume = L * W * H

# 현재 사용된 큐브 개수
now_num_cubes = 0
answer = 0

for exp, n_cube in cubes:
    # 현재 큐브 기준으로 개수를 수정해 줌
    now_num_cubes *= 8

    # 현재 큐브의 한 변의 길이
    len_cube = 2 ** exp
    
    # 현재 빈 공간에 사용할 수 있는 큐브의 최대 개수
    possible = (L // len_cube) * (W // len_cube) * (H // len_cube) - now_num_cubes
    
    # 실제로 사용된 큐브 개수
    used_cube = min(possible, n_cube)
    
    now_num_cubes += used_cube
    answer += used_cube

    # 박스를 다 채운 경우 answer 출력하고 break
    if now_num_cubes == box_volume:
        print(answer)
        break
else:
    print(-1)