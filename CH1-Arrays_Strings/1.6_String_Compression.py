class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        previous = chars[0]
        count = 1
        i = 0
        for c in chars[1:] : 
            if c == previous : # Count number of repeating characters
                count+=1
            else :
                chars[i] = previous # Append character to s 
                i+=1
                if count != 1 : # append the group's length if count is bigger than 1 
                    for n in str(count) : # append each digit seperately 
                        chars[i]=n
                        i+=1
                count = 1
                previous = c 
                
        chars[i]=previous 
        i+=1
        if count != 1 :
            for n in str(count) :
                chars[i] = n
                i+=1
        return i
