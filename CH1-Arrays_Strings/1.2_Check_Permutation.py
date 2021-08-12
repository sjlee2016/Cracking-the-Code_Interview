class Solution(object):
    def freq(self,f1, f2) :
        for i in range(27) :
            if f1[i] != f2[i] :
                return False
        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        f1 = [0] * 27
        f2 = [0] * 27

        for s in s1 :
            f1[ord(s)-ord('a')] += 1

        for i in range(0, len(s2)) :
            f2[ord(s2[i])-ord('a')]+=1
            if i >= len(s1):
                f2[ord(s2[i-len(s1)])-ord('a')]-=1
            if self.freq(f1,f2) == True :
                return True
        return False
# Use moving sliding window to find the frequency of alphabets
