class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = [0] * 27
        flag = False
        for ch in s : 
            a[ord(ch)-ord('a')] += 1
        for i in a :
            if i%2 != 0 :
                if flag : # Allow one odd number frequency 
                    return False
                else :
                    flag = True 
	return True 

# Problem 266 on leetcode 
