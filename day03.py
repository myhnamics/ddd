start = int(input('start'))
end = int(input('end'))

if end < start:
    start,end = end, start

for k in range(start,end+1):
    if k <=1:
        continue
    sosu = True
    for i in range(2,k):
        if k % i == 0:
            sosu = False
            break
    if sosu == True:
        print(k)