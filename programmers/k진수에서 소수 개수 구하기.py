import math
memo_pn = []
memo_not_pn = [1]

# 진수 변환 함수
def transform(target, k):
        # 변환 결과를 받을 변수
        v = ''
        num = target
        
        while True:
            # 몫, 나머지
            q, r = divmod(num, k)
            
            # k진법 수 변환 완료
            if not q:
                v = str(num) + v
                break
            else:
                # 나누어 떨어질 경우
                if not r:
                    v = '0' + v
                # 나누어 떨어지지 않을 경우
                else:
                    v = str(r) + v
                num = q
        return v
    
    
# 소수 체크 함수
# 소수이면 1 / 소수가 아니면 0
def check_pn(target):
    # 저장된 소수 리스트에 있으면 1 return
    if target in memo_pn:
        return 1
    # 저장된 not 소수(합성수) 리스트에 있으면 0 return
    elif target in memo_not_pn:
        return 0
    
    for i in range(2, int(math.sqrt(target))+1):
        # 나머지가 0일 경우 소수가 아니므로 0 return
        if not (target % i):
            memo_not_pn.append(target)
            return 0
            
    # 소수일 경우
    else:
        memo_pn.append(target)
        return 1
    
def solution(n, k):    
    answer = 0
    
    # 진수 변환
    target = transform(n ,k)
    
    idx = 0
    while idx < len(target):
        # 0일 경우 다음 idx로 이동
        if target[idx] == '0':
            idx += 1
            continue
            
        # 0이 아닌 숫자일 경우            
        move = idx
        move += 1
        # 다음 0이 나오는 인덱스를 찾기
        while move < len(target):
            if target[move] == '0':
                break
            move += 1
        
        # 소수 체크
        result = check_pn(int(target[idx:move]))
        if result:
            answer += 1
        
        idx = move + 1
    return answer