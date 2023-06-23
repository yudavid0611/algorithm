import sys
sys.stdin = open('1074_input.txt')

N, r, c = map(int, input().split())

delta = [[0, 0], [0, 1], [1, 0], [1, 1]]
count = 0
flag = False

def dq(row, col, n):
    global count
    global flag

    if n == 1:
        for d in delta:
            if row+d[0] == r and col+d[1] == c:
                flag = True
                break
            count += 1
        return
    else:
        # 왼쪽 위 박스
        start = [row, col]
        end = [row + 2**(n-1)-1, col + 2**(n-1)-1]
        if start[0] <= r <= end[0] and start[1] <= c <= end[1]:
            dq(row, col, n - 1)
            return
        else:
            count += (2**(n-1))**2
        
        # 오른쪽 위 박스
        start = [row, col+2**(n-1)]
        end = [row + 2**(n-1)-1, col+2**(n-1) + 2**(n-1)-1]
        if start[0] <= r <= end[0] and start[1] <= c <= end[1]:
            dq(row, col+2**(n-1), n - 1)
            return
        else:
            count += (2**(n-1))**2

        # 왼쪽 아래 박스
        start = [row+2**(n-1), col]
        end = [row+2**(n-1) + 2**(n-1)-1, col + 2**(n-1)-1]
        if start[0] <= r <= end[0] and start[1] <= c <= end[1]:
            dq(row+2**(n-1), col, n - 1)
            return
        else:
            count += (2**(n-1))**2
        
        # 오른쪽 아래 박스
        start = [row+2**(n-1), col+2**(n-1)]
        end = [row+2**(n-1) + 2**(n-1)-1, col+2**(n-1) + 2**(n-1)-1]
        if start[0] <= r <= end[0] and start[1] <= c <= end[1]:
            dq(row+2**(n-1), col+2**(n-1), n - 1)
            return
        else:
            count += (2**(n-1))**2

dq(0, 0, N)
print(count)