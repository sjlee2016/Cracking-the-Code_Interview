def urlify(s):
    space = 0
    flag = False
    startIndex = 0
    for i in range(len(s)-1,0,-1) :
        if flag is True and s[i] == ' ' :
            space+=1
        if flag is False and s[i] != ' ' :
            flag=True
            startIndex = i

    i = len(s)-1
    while startIndex >= 0 :
        if s[startIndex] == ' ' :
            s[i] = '0'
            s[i-1] = '2'
            s[i-2] = '%'
            i-=3
            startIndex-=1
        else :
            s[i] = s[startIndex]
            startIndex-=1
            i-=1

    print(''.join(s))

urlify(list("Mr John Smith    "))
