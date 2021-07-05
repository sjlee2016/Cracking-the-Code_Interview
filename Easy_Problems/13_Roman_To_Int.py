class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym = {}
        sym["I"]=1
        sym["V"]=5
        sym["X"]=10
        sym["L"]=50
        sym["C"]=100
        sym["D"]=500
        sym["M"]=1000
        value = 0
        previous = s[0]
        value+=sym[previous]
        for symbol in s[1:] :
            if sym[previous] < sym[symbol] : 
                value += (sym[symbol]-sym[previous])
                value -= sym[previous]
            else : 
                value += sym[symbol]
                previous = symbol
            
        return value
# O(n) 
