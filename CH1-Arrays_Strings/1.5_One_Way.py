# there are three types of edits that can be performed on strings
# insert a character, remove a character, or replace a character
# given two strings, write a function to check if they are one edit(or zero
# edits) away
import sys

def one_way(s1,s2):
    if len(s1) < len(s2) :
        temp = s1
        s1 = s2
        s2 = temp # let s1 be always the longer or equal size string

    if len(s1)-len(s2) > 1 :
        return False
    i = 0
    j = 0
    edit = 0
    while i < len(s1) and j < len(s2) :
        if s1[i] != s2[j] :
            if edit == 0 :
                edit = 1
            else :
                return False
            if len(s1) == len(s2) :
                j+=1
        else :
            j+=1
        i+=1

    return True
if __name__ == "__main__" :
    print(one_way(sys.argv[1],sys.argv[2]))
