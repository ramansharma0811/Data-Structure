input = [12,385,1,2846,787214]
count = 0
for i in input:
    temp = 1
    while(i//10 != 0):
        i = i//10
        temp += 1
    if (temp%2 == 0):
        count += 1
print (count)