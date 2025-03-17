cnt=int(input())
list=list(map(int, input().split()))

#print(cnt)
#print("-------------")
sum=0
arr=[]
for i in range(1, cnt) :
    #print(list[i])
    
    sum = list[i-1] + list[i]
    if(sum < 0) :
        continue
    arr.append(sum)
    

print(max(arr))