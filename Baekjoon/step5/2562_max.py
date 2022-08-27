num_list = []
for i in range(9):
    i = int(input())
    num_list += [i]
print(max(num_list))
print(num_list.index(max(num_list))+1)