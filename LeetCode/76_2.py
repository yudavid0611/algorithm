# 76. Minimum Window Substring


from collections import defaultdict
from collections import Counter
import copy
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):                                         # t가 더 길면 조건을 충족할 수 없으므로 '' 반환
            return ''

        t_dict = Counter(t)
        target = copy.deepcopy(t_dict)
        ans = ''

        left = 0
        right = 0
        while right < len(s):
            while right < len(s):
                if s[right] in target.keys():
                    target[right] -= 1
                    if list(target.values()).count(0) == len(target.keys()):
                        break
                right += 1
            ans = s[left:right+1]
            while left < len(s):
                if s[left] in target.keys():
                    ans = s[left:right+1]
                    break
                left += 1
                
        return ans