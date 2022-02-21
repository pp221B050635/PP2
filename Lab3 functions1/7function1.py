def has_33(nums):
    t=0
    for i in range(len(nums)-1):
        if(nums[i]=='3' and nums[i+1]=='3'):
            t=t+1
        else:
            t+=0
    if(t>=1):
        return 'pass'

    else:
        return 'false'


st=str(input())
st.split()
print(has_33(st))