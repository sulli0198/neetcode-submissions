class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = sorted(count, key=lambda x : count[x], reverse=True)
        return result[:k]
        