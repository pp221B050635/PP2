x = [int(i) for i in input().split()]
y = x[:]
w = True
i = 0
while i < len(x) - 1:
    if y[i] == 0:
        i -= 1
        if y[i] == 0 and i == 0:
            w = False
            break
        else:
            continue
    else:
        y[i] = 0
        i += x[i]
if w:
    print('1')
else:
    print('0')