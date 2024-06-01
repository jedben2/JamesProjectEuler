# Problem 98 - Anagramic Squares

from common import ispermutation, tqdm, np

with open("0098_words.txt", "r") as f:
    words = f.read()[1:-1].split('","')

pairs = []
for word in tqdm(words):
    for word2 in words:
        if word != word2:
            if ispermutation(word, word2):
                pairs.append([word, word2])
print(pairs)

maxsquare = 0
for pair in pairs:
    length = len(pair[0])
    squares = [i ** 2 for i in range(int(np.ceil(np.sqrt(10 ** (length - 1)))), int(np.ceil(np.sqrt(10 ** (length)))))]
    for s in squares:
        valid = True
        representation = [-1] * 10
        for i, c in enumerate(str(s)):
            if representation[int(c)] != -1:
                if representation[int(c)] != pair[0][i]:
                    valid = False
                    break
            elif pair[0][i] not in representation:
                representation[int(c)] = pair[0][i]
            else:
                valid = False
                break
        if valid:
            newsquare = ''
            for c in pair[1]:
                newsquare += str(representation.index(c))
                if int(newsquare) in squares:
                    if int(newsquare) > maxsquare:
                        maxsquare = int(newsquare)
print(maxsquare)