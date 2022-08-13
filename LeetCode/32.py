class Solution:
    def longestValidParentheses(self, s: str) -> int:
        import copy
        s_list = list(s)
        max_len = 0
        idx = 0
        count_list = [0] * len(s_list)

        while idx < len(s_list)-1:
            stack = []
            if s_list[idx] == '(':
                stack.append(s_list[idx])

                while idx < len(s_list)-1:
                    idx += 1
                    if s_list[idx] == '(':
                        if idx != len(s_list)-1:
                            stack.append(s_list[idx])
                        continue    
                    else: # s_list[idx] == ')'
                        if not stack:
                            break
                        else:
                            stack.pop()
                            count_list[idx] = 1

                for i in range(len(count_list)-1, 0, -1):
                    if count_list[i] == 1:
                        check_idx = copy.deepcopy(i)
                        cut_idx = -1

                        zero_count = 0
                        one_count = 1
                        while True:
                            check_idx -= 1
                            if count_list[check_idx] == 0:
                                zero_count += 1
                            elif count_list[check_idx] == 1:
                                one_count += 1
                            if one_count < zero_count or check_idx == -1:
                                cut_idx = check_idx
                                break

                        temp_len = 0
                        if cut_idx == -1:
                            for j in count_list[0: i+1]:
                                temp_len += j*2
                            if max_len < temp_len:
                                max_len = temp_len
                            break
                        else:
                            for j in count_list[cut_idx: i+1]:
                                temp_len += j*2
                            if max_len < temp_len:
                                max_len = temp_len
            else:
                idx += 1

        return max_len