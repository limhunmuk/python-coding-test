# 재귀호출로 수열

def recur(cnt) :
    
    if(cnt == M) :
        print(*arr)
        return
    
    #print("check = ", 1, N+1)
    for i in range(1, N+1) :
        
        #print("============= >", cnt)
    
        if i in arr : # 중복제거 부분
            #print(" 임시 출력 arr => ", *arr)
          continue
    
        arr.append(i)
        recur(cnt+1)
        arr.pop()
    

N, M = map(int, input().split())    
arr = []
print("start")
recur(0)

