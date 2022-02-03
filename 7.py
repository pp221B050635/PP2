s=str(input())
tod=int(0)
if len(s)==1:
    tod=int(s)
else:
    for i in range(len(s)):
        base=int(s[i])                        
        exp=2**(len(s)-i-1)
        '''To convert to decimal we should multiply each element of the string
        by degree of 2, which is equal to lenght s minus i and minus 1'''
        tod+=base*exp
print(tod)
    
