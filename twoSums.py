def twoSum(self, nums, target):
    # target: 9;
    #[2, 7, 11, 15]
    # {2: 0, 7: 1, 11: 3, 15: -6}
    # array.index(7)

    map = {}
    for i in range(len(nums)):
        subtracted_value = target - nums[i] # target = 2, s_v = 7
        if (subtracted_value in map.keys()):
            return [map[subtracted_value], i]
        else:
            map[nums[i]] = i
    
    return