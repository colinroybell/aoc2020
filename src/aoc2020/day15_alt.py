# From /u/xelf on Reddit thread

for part in [2020, 30000000]:
    one, nums = 19, {e: i + 1 for i, e in enumerate([16, 1, 0, 18, 12, 14])}
    for turn in range(7, part):
        nums[one], one = turn, 0 if one not in nums else turn - nums[one]
    print(one)
