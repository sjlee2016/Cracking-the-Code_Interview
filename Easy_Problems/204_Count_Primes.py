class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n<=1:
            return 0
        check = [1] * (n+1)
        check[0] = -1
        check[1] = -1
        start = 1
        ans = 0
        while start < int(sqrt(n)+1) : 
            start+=1
            if check[start]==1:
                for j in range(start*start,n,start) :
                    check[j] = -1 # check non-prime 
        for ele in check[:len(check)-1] :
            if ele == 1 :
                ans+=1 
        return ans
