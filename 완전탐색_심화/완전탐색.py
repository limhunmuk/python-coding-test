# 재귀호출로 수열

def recur(cnt) :
    
    if(cnt == M) :
    
        print(*arr)
        return
    
    
    for i in range(1, N+1) :
        
        print("============= >", cnt)
    
        if i in arr :
            continue
        
        arr.append(i)
        recur(cnt+1)
        arr.pop()
    

N, M = map(int, input().split())    
arr = []
recur(0)

