numbers=[]
n=int(input())
for i in range(n):
    numbers.append(int(input()))
for i in range(n):
    if numbers[i] <= 10:                                    #I create the for loop for checking all values of i
        print("Go to work!")
    elif numbers[i] > 10 and numbers[i] <= 25:
        print("You are weak")
    elif numbers[i] > 25 and numbers[i] <= 45:
        print("Okay, fine")
    elif numbers[i] > 45:
        print("Burn! Burn! Burn Young!")