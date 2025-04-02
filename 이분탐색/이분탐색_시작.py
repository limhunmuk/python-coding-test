# 첫재줄 n -> 숫자 카드 개스
# 둘째 줄 숫자 카드 정수 ( 동일 한 숫자 없음 )
# 숫자 M
# 상근이가 가지고 있는 카드인지 확인해야될 정수 리스트
#5
#6 3 2 10 -10
#8
#10 9 -5 2 3 4 5 -10

n = int(input())
arr1 = sorted(list(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split()))

result = []

#for i in range(n) :
#    print(" i > ", arr1[i])
    

# 비교 값 루프를 돌면서
for j in range(m) :
    #print(" j > ", arr2[j])
    
    s = 0
    e = (n - 1)
      
    flag = False
    
    # while 문으로 정렬된 arr1 시작점 , 끝 점을 이분 탐색하며 이동
    # 바깥쪽 포문[j] == arr2 > 하나씩 꺼내 arr1에 있는값이면 1 없으면 0
    # result에 담아서 리턴할것
    while( s <= e ) :
        mid = (s + e) // 2
        if(arr2[j] == arr1[mid]) :
            flag = True
            break
        elif(arr2[j] < arr1[mid]) :
            e = mid - 1
        else :
            s = mid + 1        
    
    if(flag) :
        result.append(1)
    else :
        result.append(0)
        
        
print(*result)
        

        
        

  

