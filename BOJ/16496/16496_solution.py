import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
sys.stdin = open('16496_input.txt')
input = sys.stdin.readline


def sort_nums(nums:list, depth:int):
    # depth 인덱스의 숫자에 따라 숫자 nums 분리
    splited_nums = defaultdict(list)

    # nums 숫자들 중 최대 자릿수
    max_len = 0
    
    for num in nums:
        if len(num) > max_len:
            max_len = len(num)

        revised_depth = depth % len(num)
        splited_nums[num[revised_depth]].append(num)
    
    # depth가 max_len * 2와 동일하면 nums를 더 이상 정렬할 필요 없음
    # 왜냐하면 max_len * 2의 depth에서는 비교 과정에서 사이클이 발생하기 때문
    if depth == max_len * 2:
        return ''.join(nums)
    
    result = ''

    # 9부터 0까지 순회
    for digit in range(9, -1, -1):
        i = str(digit)
        
        # 숫자 없음
        if not splited_nums[i]:
            continue
        
        # 숫자 1개
        elif len(splited_nums[i]) == 1:
            result += splited_nums[i][0]
        
        # 숫자 2개 이상
        else:
            sorted_nums = sort_nums(splited_nums[i], depth+1)
            result += sorted_nums
    return result
    

if __name__ == '__main__':
    N = int(input().rstrip())
    nums = input().split()
    
    result = sort_nums(nums, 0)
    if result[0] == '0':
        print('0')
    else:
        print(result)