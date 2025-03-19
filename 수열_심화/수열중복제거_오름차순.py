def recur(start, depth) :
    
    if(depth == M) :
        print(*arr)
        return
    
    for i in range(start, N+1) :
       
        # 중복제거
        #if i in arr :
        #  continue
        #if visited[i] :
        #    continue
      
       # visited[i] = 1
        arr.append(i)
        recur(i+1, depth+1)
        arr.pop()
        #visited[i] = 0


N, M = map(int, input().split())    
arr = []
#visited = [0 for _ in range(N+1)]
recur(1, 0)

