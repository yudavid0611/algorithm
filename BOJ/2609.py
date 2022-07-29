nums = list(map(int, input().split()))

if nums[0] == nums[1]:
    print(nums[0])
    print(nums[0])
else:
    init_divior = 1
    max_divior = 1

    while True:
        if nums[0] % 2 == 0 and nums[1] % 2 == 0:
            init_divior *= 2
            nums[0] = nums[0] / 2
            nums[1] = nums[1] / 2
        else:
            break
    nums[0] = int(nums[0])
    nums[1] = int(nums[1])

    if nums[0] > nums[1]:
        big = nums[0]
        small = nums[1]
    else:
        big = nums[1]
        small = nums[0]


    for i in range(small, 0, -1):
        if (big % i == 0) and (small % i == 0):
            max_divior *= i
            break

    min_mulpiple = (nums[0]/max_divior) * (nums[1]/max_divior) * init_divior * max_divior

    print(init_divior * max_divior)
    print(int(min_mulpiple))
