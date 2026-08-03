class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        ans = 0
        currentOnes = 0
        for i in range(len(nums)):
            if (nums[i]==0):
                currentOnes = 0
            else :
                currentOnes +=1

            if (currentOnes > ans) :
                ans = currentOnes

        return ans



       

      