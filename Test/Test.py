class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length=len(nums)
        index=0
        total=0
        while index<k:
            total=total+nums[index]
            index=index+1
        index=1
        med=total
        while index<length-k+1:
            med=med-nums[index-1]+nums[index+k-1]
            if med>total:
                total=med
            index=index+1
        return total/k

A=Solution()
k=1
nums=[1,12,-5,-6,50,3]
total=A.findMaxAverage(nums,k)
print(str(total))

