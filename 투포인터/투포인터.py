#3273

# 우선 정렬
# 기준 숫자보다 큰 숫자는 지우기

A = int(input())
arr = sorted(list(map(int, input().split())))
C = int(input())

#print(A)
#print("=============")
#for i in range(A) :
#    print(arr[i])
    

#print("=============")
#print(C)

#print("=============")

S=0
E=A-1
CNT=0

while(S < E) :
    if arr[S] + arr[E] == C :
        CNT += 1
    
    if arr[S] + arr[E] >= C :
        E -= 1
    else :
        S += 1

print(CNT)