nums = list(map(int, input().split()))
new_num1 = str()
new_num2 = str()
for i in range(2, -1, -1):
    new_num1 += str(nums[0])[i]
    new_num2 += str(nums[1])[i]
if int(new_num1) > int(new_num2):
    print(new_num1)
else:
    print(new_num2)