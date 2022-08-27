N = int(input())
score = list(map(int, input().split()))

m = max(score)
new_score = []
for i in score:
    new_score.append(i/m*100)
my_avg = sum(new_score) / len(new_score)
print(my_avg)