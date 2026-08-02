class Solution(object):
    def maxSubArray(self, nums):
        maxNo = nums[0]
        currentSum = nums[0]
        for i in range(1,len(nums)):
            if currentSum < 0:
                currentSum = 0
            currentSum+= nums[i]

            if currentSum > maxNo:
                maxNo = currentSum

        return maxNo
        