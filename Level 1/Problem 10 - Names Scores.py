# Names Scores

from string import ascii_uppercase

with open("0022_names.txt", "r") as f:
    namestemp = f.read()
names = sorted(namestemp[1:-1].split('","'))

scores = []
for index, name in enumerate(names):
    score = 0
    listname = list(name)
    for char in name:
        score += ascii_uppercase.find(char) + 1
    scores.append(score * (index + 1))
print(sum(scores))
