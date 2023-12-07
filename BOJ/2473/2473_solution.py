import sys
sys.stdin = open('2473_input.txt')
input = sys.stdin.readline

N = int(input().rstrip())
liquid = sorted(map(int, input().split()))

answer = [30000000001, 0, 0, 0]
found_zero = False
for i in range(0, N - 2):
    left = i + 1
    right = N - 1

    fixed_liquid = liquid[i]

    # 두 포인터가 만나면 break
    while left < right:
        new_liquid = fixed_liquid + liquid[left] + liquid[right]

        # 새로운 조합이 0에 더 가까울 경우 answer 업데이트
        if abs(new_liquid) < answer[0]:
            answer[0], answer[1], answer[2], answer[3] = abs(new_liquid), fixed_liquid, liquid[left], liquid[right]
        
        if new_liquid == 0:
            found_zero = True
            break

        elif new_liquid > 0:
            right -= 1
        
        else:
            left += 1
    
    if found_zero:
        break

print(f'{answer[1]} {answer[2]} {answer[3]}')