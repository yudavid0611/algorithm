first_10 = [1,1,1,2,2,3,4,5,7,9]
number_unipue = [1,2,3,4,5,7,9]
temp = []
start_1 = 9
start_2 = 3
for i in range(90):
    temp.append(start_1 + start_2)
    start_1 = start_1 + start_2
    start_2 = number_unipue[3+i]
    number_unipue.append(start_1)
total = first_10 + temp

tc = int(input())
for t in range(tc):
    n = int(input())
    print(total[n-1])