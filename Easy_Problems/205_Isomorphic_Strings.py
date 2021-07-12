class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        dic2 = {}
        i = 0
        if len(s) != len(t) :
            return False 
        
        for ch in s :
            if ch not in dic :
                if t[i] in t[:i] :
                    return False 
                dic[ch] = t[i]
            else : 
                value = dic[ch] 
                if value is not t[i] : 
                    return False 
            i+=1
            
        return True
