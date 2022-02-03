s=input()
result=0
for i in s:
  result += ord(i)  #I am summing ascii of all characters
if result > 300:
    print("It is tasty!")
else:
    print("Oh, no!")