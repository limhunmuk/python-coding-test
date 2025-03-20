def recur(start, depth) :
    if(depth == M) :
        print(*arr)
        return


    for i in range(start, N+1) :
        
        arr.append(i)
        recur(i, depth+1)
        arr.pop()
        
        
        
        
        
N, M = map(int, input().split())
arr = []
recur(1, 0)