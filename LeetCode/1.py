from collections import defaultdict

class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = defaultdict(list)
        
        # key는 숫자, value는 인덱스
        for idx, n in enumerate(nums):
            nums_dict[n].append(idx)
        
        for k, v in nums_dict.items():
            pair_k = target - k
            pair_v = nums_dict.get(pair_k, -1)
            
            # 쌍을 이루는 숫자가 존재할 경우
            if pair_v != -1:

                # 같은 숫자일 경우
                if pair_k == k:
                
                    # 인덱스가 다를 때
                    if len(v) != 1:
                        return [v[0], v[1]]
                
                else:
                    return [v[0], pair_v[0]]