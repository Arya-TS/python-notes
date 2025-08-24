n = int(input())
l2 = []
for _ in range(n):
    name = input()
    score = float(input())
    l2.append([name, score])

scores = sorted({i[1] for i in l2})
sec_lowest_score = scores[1]

names = [i[0] for i in l2 if i[1] == sec_lowest_score]

names.sort()

for i in names:
    print(i)
