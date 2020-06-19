inputArray = [1,1,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0]
count=0
count1=0
for i in inputArray:
    if(i == 1):
        count = count+1
    else:
        count =0
    if(count1<count):
        count1 = count
print(count1)