# 1931: 회의실 배정


import sys
sys.stdin = open('1931_input.txt')
N = int(input())

meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append([s, e])
# 시작 시간을 기준으로 정렬
meetings.sort()

now_meeting = meetings[0]
count = 1
for i in range(1, N):
    # now_meeting의 끝나는 시간 안쪽에 meetings[i]가 위치할 경우 now_meeting 갱신
    if now_meeting[1] > meetings[i][0] and now_meeting[1] > meetings[i][1]:
        now_meeting = meetings[i]
    # now_meeting이 끝난 경우 count +1 해주고 now_meeting 갱신
    elif now_meeting[1] <= meetings[i][0]:
        count += 1
        now_meeting = meetings[i]

print(count)