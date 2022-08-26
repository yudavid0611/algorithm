import sys
sys.stdin = open('BOJ/1244/1244_input.txt', 'r')

switch_num = int(input())

switch = list(map(int, input().split()))
switch.insert(0,0)                                                                      # 스위치 번호가 1번부터 시작하기에 앞에 0을 추가해줌

student_num = int(input())

student = [list(map(int, input().split())) for _ in range(student_num)]

delta = [-1, 1]                                                                         # 여학생의 스위치 작업을 위해 delta 정의
for s in student:
    n = s[1]                                                                            # 현재 학생이 가지고 있는 숫자
    
    if s[0] == 1:                                                                       # 남학생인 경우,
        multiple = 2
        while n < switch_num+1:                                                         # 숫자의 배수가 스위치 개수를 넘지 않을 때까지 순회
            switch[n] = 1 if switch[n] == 0 else 0                                      # 스위치 상태 바꾸기
            n = (s[1]) * multiple
            multiple += 1
    
    else:                                                                               # 여학생인 경우,
        multiple = 0
        while True:
            left = n+delta[0]*(multiple+1)                                              # 체크할 왼쪽 스위치
            right = n+delta[1]*(multiple+1)                                             # 체크할 오른쪽 스위치
            if left > 0 and right <= switch_num and switch[left] == switch[right]:      # 스위치가 스위치 범위에 포함되어 있고, 대칭일 경우
                multiple += 1                                                           # 다음 범위 체크를 위해 multiple + 1
            else:
                break

        for i in range(n+delta[0]*multiple, n+delta[1]*multiple+1):                     # 스위치 상태를 변경할 범위(대칭인 범위)를 순회
            switch[i] = 1 if switch[i] == 0 else 0                                      # 스위치 상태 변경

for idx, i in enumerate(switch[1:], 1):
    print(str(i), end=' ')
    if idx % 20 == 0:
        print()