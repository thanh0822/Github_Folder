def list_mean(nums):
    sumof = 0
    num_of = len(nums)
    mean = 0
    for i in nums:
        sumof += i
    mean = sumof / num_of
    return float(mean)
