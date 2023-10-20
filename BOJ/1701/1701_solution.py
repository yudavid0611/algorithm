import sys
sys.stdin = open('1701_input.txt')
input = sys.stdin.readline

text = input().rstrip()
len_text = len(text)

# 실패함수
def failure(pattern):
    # 해당 인덱스까지 prefix와 suffix가 일치하는 최대 길이를 저장
    arr = [0] * len(pattern)
    
    # j: prefix 인덱스, i: suffix 인덱스
    j = 0
    for i in range(1, len(pattern)):
        # j가 0이거나, i와 j의 철자가 다를 때까지 j 이동시키기
        while j > 0 and pattern[i] != pattern[j]:
            j = arr[j-1]
        
        # 패턴이 일치할 경우 i 인덱스에 j + 1 값을 저장
        if pattern[i] == pattern[j]:
            j += 1
            arr[i] = j

    return max(arr)

answer = 0
for i in range(len_text):
    # 나올 수 있는 모든 패턴을 고려하기
    result = failure(text[i:])
    if result > answer:
        answer = result
print(answer)