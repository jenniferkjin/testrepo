def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        elem1 = nums[0]
        return elem1
    else:
        elem1 = nums[0]
        elem2 = nums[1]
        return elem1 + elem2


sum2([1, 2, 3])
