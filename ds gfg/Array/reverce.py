def reverseWord(s):
    start=0
    end=len(s)-1
    while(start<end):
        s[start],s[end]=s[end],s[start]
        start+=1
        end-=1
    return s

# 
reverse_String = "" 
    count = len(s) 
    while count > 0:
        reverse_String += s[ count - 1 ] 
        count = count - 1 
    return reverse_String