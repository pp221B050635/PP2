year=int(input())
def Leap(x):
    if x%400==0 or x%100!=0 and x%4==0:
        return('The year is leap')
    else:
        return('The year is not leap')
print(Leap(year))