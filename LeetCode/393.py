# 393. UTF-8 Validation

# flow
# 1. data의 첫 번째 원소로 몇 바이트 문자인지 확인
# 2. 바이트에 따른 sequence가 유효한지 판별 

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check_bytes(element):
            if element[0] == '0':
                return 0
            elif element[:3] == '110':
                return 1
            elif element[:4] == '1110':
                return 2
            elif element[:5] == '11110':
                return 3
            else:
                return False
        

        while data:
            element = bin(data.pop(0))[2:]
            check_nums = check_bytes(element)
            if check_nums == False:
                return False
            
            result = True
            while check_nums > 0:
                sequence = bin(data.pop(0))[2:]
                if sequence[:2] != '10':
                    result = False
                    break
                check_nums -= 1
            if not result:
                return False
        return True