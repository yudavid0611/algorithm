non_self_number_list = []
for i in range(1, 10000+1):
    new_number = int()
    for j in str(i):
        new_number += int(j)
    new_number += i
    non_self_number_list.append(new_number)

temp_set = set([i for i in range(1, 10000+1)])
non_self_number_set = set(non_self_number_list)

self_number_list = sorted(list(temp_set - non_self_number_set), reverse=False)

for i in self_number_list:
    print(i)