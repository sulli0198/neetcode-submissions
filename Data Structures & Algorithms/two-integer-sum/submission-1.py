class Solution:
    def twoSum(self, nums, target):
        count = {}

        for i in range(len(nums)):
                complement = target - nums[i]
                if complement in count:
                    return [count[complement], i]
                else:
                    count[nums[i]] = i



        