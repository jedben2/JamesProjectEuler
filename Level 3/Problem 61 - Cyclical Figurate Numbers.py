# Problem 61 - Cyclical Figurate Numbers

from common import pnumber, solvepnumber
import sys

for a in range(45, 141):
    nums = [4, 5, 6, 7, 8]
    n1 = pnumber(3, a)
    for b in range(0, 100):
        n2 = int(str(n1)[2:] + str(b).zfill(2))
        if len(str(n2)) == 4:
            valid = [solvepnumber(i, n2) % 1 == 0 for i in nums]
            if any(valid):
                nums2 = [nums[i] for i in range(len(nums)) if not valid[i]]
                for c in range(0, 100):
                    n3 = int(str(n2)[2:] + str(c).zfill(2))
                    if len(str(n3)) == 4:
                        valid = [solvepnumber(i, n3) % 1 == 0 for i in nums2]
                        if any(valid):
                            nums3 = [nums2[i] for i in range(len(nums2)) if not valid[i]]
                            for d in range(0, 100):
                                n4 = int(str(n3)[2:] + str(d).zfill(2))
                                if len(str(n4)) == 4:
                                    valid = [solvepnumber(i, n4) % 1 == 0 for i in nums3]
                                    if any(valid):
                                        nums4 = [nums3[i] for i in range(len(nums3)) if not valid[i]]
                                        for e in range(0, 100):
                                            n5 = int(str(n4)[2:] + str(e).zfill(2))
                                            if len(str(n5)) == 4:
                                                valid = [solvepnumber(i, n5) % 1 == 0 for i in nums4]
                                                if any(valid):
                                                    nums5 = [nums4[i] for i in range(len(nums4)) if not valid[i]]
                                                    n6 = int(str(n5)[2:] + str(n1)[:2])
                                                    if len(str(n6)) == 4 and solvepnumber(nums5[0], n6) % 1 == 0:
                                                        print(n1, n2, n3, n4, n5, n6)
                                                        print(sum([n1, n2, n3, n4, n5, n6]))
                                                        sys.exit("Done!")
