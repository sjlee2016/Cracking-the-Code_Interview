def palindrome(s) :
    alpha = [0] * 128
    for c in s :
        if c is not ' ' :
            if ord(c) >= ord('A') and ord(c) <= ord('Z'): ## convert Capitalized to lowercase
                alpha[ord(c)-ord('A')]+=1
            else :
                alpha[ord(c)-ord('a')]+=1

    flag = False

    for i in range(128) :
        if alpha[i]%2==1 :
            if flag == True :
                return False
            else :
                flag = True

    return True


print(palindrome("tact Coa"))
