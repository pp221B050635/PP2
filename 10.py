s=str(input())
s1=s.split()
s2 =" ".join([s for s in s1 if len(s)>=3])
print(s2)