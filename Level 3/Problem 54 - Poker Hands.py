# Problem 54 - Poker Hands

# Rankings:
# Royal Flush = 10
# Straight Flush = 9
# Four of a kind = 8
# Full House = 7
# Flush = 6
# Straight = 5
# Trips = 4
# Two pair = 3
# Pair = 2
# High = 1

# Sorry this is aids :/

def isstraight(nums):
    if sorted(nums) == [2, 3, 4, 5, 14]:
        return True
    for i in range(1, 11):
        if [j for j in range(i, i + 5)] == sorted(nums):
            return True
    return False


def isflush(suits):
    if len(set(suits)) == 1:
        return True
    return False


def reducehand(hand):
    nums = list(hand.replace(" ", "")[0:-1:2])
    for i in range(len(nums)):
        if nums[i] == "T":
            nums[i] = 10
        elif nums[i] == "J":
            nums[i] = 11
        elif nums[i] == "Q":
            nums[i] = 12
        elif nums[i] == "K":
            nums[i] = 13
        elif nums[i] == "A":
            nums[i] = 14
    nums = [int(i) for i in nums]
    suits = list(hand.replace(" ", "")[1::2])
    return nums, suits


def characterisehand(hand):
    nums, suits = reducehand(hand)

    if isflush(suits):
        if isstraight(nums):
            if 14 in nums and 13 in nums:
                return 10, max(nums)
            else:
                return 9, max(nums)
        else:
            return 6, max(nums)
    elif isstraight(nums):
        return 5, max(nums)
    elif len(set(nums)) == 4:
        return 2, max(nums)
    elif len(set(nums)) == 3:
        for n in nums:
            if nums.count(n) == 3:
                return 4, max(nums)

        return 3, max(nums)
    elif len(set(nums)) == 2:  # full house or four of a kind
        if nums.count(nums[0]) in [1, 4]:
            return 8, max(nums)
        else:
            return 7, max(nums)
    else:
        return 1, max(nums)

def findpairs(nums):
    pairs = set()
    for n in nums:
        if nums.count(n) == 2:
            pairs.add(n)
    return list(pairs)
def findthree(nums):
    for n in nums:
        if nums.count(n) == 3:
            return n
    return None

def findfour(nums):
    nums2 = set(nums)
    if nums.count(nums2[0]) == 4:
        return nums2[0]
    return nums2[1]
def findwin(game):
    p1 = game[:14]
    p2 = game[15:]
    c1, p1high = characterisehand(p1)
    c2, p2high = characterisehand(p2)
    if c1 == c2:
        p1nums = reducehand(p1)[0]
        p2nums = reducehand(p2)[0]
        if c1 == 1 or c1 == 5 or c1 == 6 or c1 == 9:
            if p1high > p2high:
                return 1
            elif p1high == p2high:
                p1nums.remove(p1high)
                p2nums.remove(p2high)
                if max(p1nums) > max(p2nums):
                    return 1
                else:
                    return 0
            else:
                return 0
        elif c1 == 2:
            p1pair = findpairs(p1nums)
            p2pair = findpairs(p2nums)
            if p1pair[0] > p2pair[0]:
                return 1
            elif p1pair[0] == p2pair[0]:
                p1nums = [i for i in p1nums if i not in p1pair]
                p1nums = [i for i in p2nums if i not in p2pair]
                if max(p1nums) > max(p2nums):
                    return 1
                else:
                    return 0
            else:
                return 0
        elif c1 == 3:
            p1pair = findpairs(p1nums)
            p2pair = findpairs(p2nums)
            if max(p1pair) > max(p2pair):
                return 1
            elif max(p1pair) == max(p2pair) and min(p1pair) > min(p2pair):
                return 1
            elif sorted(p1pair) == sorted(p2pair):
                p1nums = [i for i in p1nums if i not in p1pair]
                p1nums = [i for i in p2nums if i not in p2pair]
                if p1nums[0] > p2nums[0]:
                    return 1
                else:
                    return 0
            else:
                return 0
        elif c1 == 4:
            p1trip = findthree(p1nums)
            p2trip = findthree(p2nums)
            if p1trip > p2trip:
                return 1
            else:
                return 0
        elif c1 == 8:
            p1four = findfour(p1nums)
            p2four = findfour(p2nums)
            if p1nums > p2four:
                return 1
            else:
                return 0
        else:
            p1three = findthree(p1nums)
            p2three = findthree(p2nums)
            p1pair = findpairs(p1nums)
            p2pair = findpairs(p2nums)
            if p1three > p2three:
                return 1
            elif p1three == p2three and p1pair[0] > p2pair[0]:
                return 1
            else:
                return 0

    elif c1 > c2:
        return 1
    else:
        return 0


with open("0054_poker.txt", "r") as f:
    games = f.readlines()
    games = [g.strip() for g in games]

p1wincount = 0
for game in games:
    p1wincount += findwin(game)
print(p1wincount)
