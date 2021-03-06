#Contains Duplicate II
#Given an array of integers and an integer k,
#find out whether there there are two distinct indices i and j in the array
#such that nums[i] = nums[j] and the difference between i and j is at most k.

#2015年6月8日   AC
#zss

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numDir = {}
        length = len(nums)
        for i in range(length):
            j = numDir.get(nums[i])
            if j!=None and i-j<=k:
                return True
            else:
                numDir[nums[i]]=i
        return False
