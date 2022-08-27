num = input().split()
num_list = []
for i in num:
    i1 = i[::-1]
    num_list += [i1]
if num_list[0] > num_list[1]:
    print(num_list[0])
else:
    print(num_list[1])