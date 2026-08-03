class Solution(object):
    def maxProduct(self, nums):
        minValue = 0
        maxValue = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                maxValue = (nums[i]-1)*(nums[j]-1)
                if minValue < maxValue:
                    minValue = maxValue   
        return minValue

        
        