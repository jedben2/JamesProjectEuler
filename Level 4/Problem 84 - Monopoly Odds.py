# Problem 84 - Monopoly Odds

# Community Chest (2/16 cards):
# 1 - Advance to GO (00)
# 2 - Go to JAIL (10)

# Chance (10/16 cards):
# 1 - Advance to GO (00)
# 2 - Go to JAIL (10)
# 3 - Go to C1 (11)
# 4 - Go to E3 (24)
# 5 - Go to H2 (39)
# 6 - Go to R1 (05)
# 7 - Go to next R (railway company) (odd multiple of 5 above position)
# 8 - Go to next R (odd multiple of 5 above position)
# 9 - Go to next U (utility company) (12 or 28)
# 10 - Go back 3 squares

import random
from tqdm import tqdm

CCcards = [i for i in range(1, 17)]
CHcards = [i for i in range(1, 17)]

random.shuffle(CCcards)
random.shuffle(CHcards)

frequencies = [0] * 40
doubles = 0
position = 0


def rolldie(n):  # sum of two rolls of an n sided die, is a double
    r1, r2 = random.randint(1, n), random.randint(1, n)
    return r1 + r2, r1 == r2


def playturn(position):  # Returns the final position after a roll of the dice
    global doubles, CHcards, CCcards
    diff, isdouble = rolldie(4)
    if isdouble:
        doubles += 1
        if doubles == 3:  # 3x doubles in a row -> jail
            doubles = 0
            return 10
    else:
        doubles = 0
    position += diff
    position = position % 40
    if position == 30:  # G2J square
        return 10
    elif position in (2, 17, 33):  # CC card
        card = CCcards[0]
        CCcards = CCcards[1:] + [CCcards[0]]
        if card == 1:
            return 0
        elif card == 2:
            return 10
        else:
            return position
    elif position in (7, 22, 36):
        card = CHcards[0]
        CHcards = CHcards[1:] + [CHcards[0]]
        if card == 1:
            return 0
        elif card == 2:
            return 10
        elif card == 3:
            return 11
        elif card == 4:
            return 24
        elif card == 5:
            return 39
        elif card == 6:
            return 5
        elif card in (7, 8):
            if position == 7:
                return 15
            elif position == 22:
                return 25
            else:
                return 5
        elif card == 9:
            if 12 < position and position < 28:
                return 28
            else:
                return 12
        elif card == 10:
            return position - 3
        else:
            return position
    else:
        return position


numturns = 1000000
for turn in tqdm(range(numturns)):
    position = playturn(position)
    frequencies[position] += 1

maxfreqs = [0] * 3
for i in range(40):
    if frequencies[i] > min(maxfreqs):
        maxfreqs.remove(min(maxfreqs))
        maxfreqs.append(frequencies[i])
maxfreqs = sorted(maxfreqs)[::-1]
print(''.join(["{:02d}".format(frequencies.index(f)) for f in maxfreqs]))
