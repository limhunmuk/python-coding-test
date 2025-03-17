cnt=int(input())
list=list(map(int, input().split()))

prefix=[0 for _ in range(cnt + 1)];



for i in range(cnt) :
    prefix[i + 1] = max(prefix[i] + list[i], list[i])
    

prefix.pop(0)
print(max(prefix))

