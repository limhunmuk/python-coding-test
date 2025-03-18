# 재귀호출로 수열

def recur(cnt) :
    
    if(cnt == M) :
    
        print(*arr)
        return
    
    #print("check = ", 1, N+1)
    for i in range(1, N+1) :
        
        #print("============= >", cnt)
    
       #if i in arr :
       #     continue
               
        arr.append(i)
        #print("print => ", *arr)
        recur(cnt+1)
        arr.pop()
    

N, M = map(int, input().split())    
arr = []
print("start")
recur(0)

