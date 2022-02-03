s=str(input())
low=0
def toLowercase(s):
    s=str(s)
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            low=chr(ord(i)+32)
            s=s.replace(i, low)
    print(s)



toLowercase(s)
