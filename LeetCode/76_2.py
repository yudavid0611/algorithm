# 76. Minimum Window Substring
# 575ms / 14.8mb


from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):                                         # t가 더 길면 조건을 충족할 수 없으므로 '' 반환
            return ''

        target = Counter(t)
        target_keys = target.keys()
        result = '0' * (len(s) + 1)

        left = 0
        right = 0
        while right < len(s):
            left_flag = False
            while right < len(s):
                if s[right] in target_keys:
                    target[s[right]] -= 1
                    if len(list(filter(lambda x: x <= 0, list(target.values())))) == len(target):
                        right += 1
                        left_flag = True
                        break
                right += 1
            while left_flag and left < len(s):
                if s[left] in target_keys:
                    target[s[left]] += 1
                    if target[s[left]] > 0:
                        if len(result) > len(s[left:right]):
                            result = s[left:right]
                        left += 1
                        break
                left += 1
        return result if len(result) != (len(s) + 1) else ''