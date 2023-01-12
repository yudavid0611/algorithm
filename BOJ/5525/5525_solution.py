# 5525: IOIOI


import sys
sys.stdin = open('5525_input.txt')

N = int(input())
m = int(input())
s = input()

result = 0
while True:
    # 시작점이 될 I 인덱스
    idx = s.find('I')
    base = idx

    while True:
        if idx == m or idx == -1 or s[idx] != 'I':
            break
        idx += 1
        if idx == m or idx == -1 or s[idx] != 'O':
            break
        idx += 1
    
    # 마지막 인덱스에서 멈춰있는 경우 break
    if base == idx:
        break

    # IO패턴이 유효한 구간에서 'O'의 개수 세기
    count_O = s[base:idx].count('O')
    if count_O >= N:
        # 유효한 구간의 마지막 문자가 'I'인 경우
        if s[idx-1] == 'I':
            result += count_O - N + 1
        # 유효한 구간의 마지막 문자가 'O'인 경우
        else:
            result += count_O - N
    
    # 사용한 문자열 구간은 제거
    s = s[idx:]
    # 문자열 길이 업데이트
    m = len(s)

print(result)