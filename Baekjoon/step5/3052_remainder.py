num = []
for i in range(10):
    n = int(input())
    num.append(n % 42)

new_num = set(num)
print(len(new_num))