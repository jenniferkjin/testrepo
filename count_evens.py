def count_evens(nums):
    even_num = 0
    for i in nums:
        if i % 2 == 0:
            even_num = even_num + 1
    return even_num
