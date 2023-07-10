from collections import defaultdict

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digits = []
        letters = defaultdict(list)

        for log in logs:
            space_idx = log.find(' ')
            # digit log일 경우 digits에 append
            if log[space_idx + 1].isdigit():
                digits.append(log)
            
            # letter log일 경우 letters에 단어를 key로 하여 identifier를 append
            else:
                letters[log[space_idx + 1:]].append(log[:space_idx])

        # 단어 기준 오름차순 정렬
        letters = sorted(letters.items())
        
        answer = []
        for word, idt in letters:
            # 중복단어가 아닐 경우 answer에 바로 append
            if len(idt) == 1:
              answer.append(idt[0] + ' ' + word)
            # 중복 단어일 경우
            else:
                # identifier 오름차순 정렬
                idt.sort()
                for i in idt:
                    answer.append(i + ' ' + word)
        
        # letter logs와 digit logs 합치기
        answer.extend(digits)
        return answer