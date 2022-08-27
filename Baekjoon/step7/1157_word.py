w = input().upper()
word = list(set(w))

cnt_list = []
for i in word:
    cnt_list.append(w.count(i))
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(word[cnt_list.index(max(cnt_list))])