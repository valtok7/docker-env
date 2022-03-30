import csv
import random
from typing import ByteString
with open("src/agaricus-lepiota.data") as fp:
    table = list(csv.reader(fp))

random.shuffle(table)
train = table[:7000]
test = table[7000:]


def findbest(a):
    c = {}
    for x in a:
        if x in c:
            c[x] += 1
        else:
            c[x] = 1

    best = a[0]
    for x in c.keys():
        if c[best] < c[x]:
            best = x
    return best


for i in range(22):
    feats = {}
    for row in train:
        answer = row[0]
        f = row[i + 1]
        if not (f in feats):
            feats[f] = []
        feats[f].append(answer)

    rule = {}
    for f in feats.keys():
        rule[f] = findbest(feats[f])

    score = 0
    for row in test:
        answer = row[0]
        if (f in rule) and (rule[f] == answer):
            score = score + 1
    print(f"使った特徴量:{i+1}")
    print(f"使った規則:{rule}")
    print(f"スコア:{score}")
