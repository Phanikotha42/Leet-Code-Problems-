class Solution(object):
    def findMissingElements(self, nums):
        A = []
        B = []
        nums.sort()
        maxNum = nums[-1]
        minNum = nums[0]
        for i in range(minNum,maxNum+1):
            A.append(i)
        for i in A:
            if i not in nums:
                B.append(i)
        return B
            
            