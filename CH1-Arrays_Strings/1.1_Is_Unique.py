# Problem 217 on leetcode
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for n in nums :
            if n in dic :
                return True
            else :
                dic[n] = 1
        return False

# Using sort and find duplicate if O(nlogn) but using hash table
# gives u O(n).
