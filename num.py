def twosum(nums, target):

    dic = {}
    for i in range(len(nums)):
        if target - nums[i] not in dic:
            dic[nums[i]] = i
        else:
            ans = [dic[target - nums[i]], i] 
    return ans
