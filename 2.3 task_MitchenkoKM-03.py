k = 0
x = int(input('Minutes'))
if x < 0:
    print('Its negative')
else:
    if 0 <= x <= 50:
        k = k+100
    elif 50 < x <= 100:
        k = k+150
    elif x > 100:
        b = x - 100
        k = k + 150 + b*2
print(k)