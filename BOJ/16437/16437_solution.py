import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
sys.stdin = open('16437_input.txt')
input = sys.stdin.readline

def postorder(v):
    # 루트
    if not tree[v]:
        # 양이 있을 경우
        if animal_list[v][0] == 'S':
            return animal_list[v][1]
        else:
            return 0
    else:
        all_sheep = 0
        for child in tree[v]:
            all_sheep += postorder(child)
        
        # 현재 섬에 있는 동물이 양일 경우
        if animal_list[v][0] == 'S':
            return all_sheep + animal_list[v][1]
        # 현재 섬에 있는 동물이 늑대일 경우
        else:
            return max(0, all_sheep - animal_list[v][1])

if __name__ == '__main__':
    N = int(input().rstrip())
    tree = defaultdict(list)
    animal_list = [0] * (N + 1)
    animal_list[1] = ['S', 0]
    for i in range(2, N + 1):
        animal, animal_num, v = input().split()
        tree[int(v)].append(i)
        animal_list[i] = [animal, int(animal_num)]
    
    print(postorder(1))