s = int()
for i in range(1, 501, 1):
    if i % 3 == 0 and i%2!=0:
        s += i
print(s)
