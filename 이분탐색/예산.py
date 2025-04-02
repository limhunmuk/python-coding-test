cnt = int(input())
arr = list(map(int, input().split()))
money = int(input())

print(*arr)
    
start = 0
end = money
result = 0

while(start <= end) :
    
    #이분검색 시작
    mid = (start + end) // 2
    
    benefit = money

    # [ex] arr = [120 110 140 150]
    # given 485    
  
    total = 0
   # arr2 = []
    for reqMoney in arr :
        
        # reqMoney 가 중간값(분할값) 보다 큰지
        #if mid >= reqMoney :
        if reqMoney > mid :
            
            # 배분 값이 요청값보다 크면 모두 삭감
            # benefit -= reqMoney
            total += mid # 요청값이 할당 금액보다 크면
        else :
            # 배분값이 요청값보다 작으면 배분값만큼만 삭제
            #reqMoney = (reqMoney - mid)
            # benefit -= reqMoney
            # 요청 값이 배분값(분할값) 보다
            total += reqMoney
            
        # 이때 모든 요청한 만큼 금액을 적당히주고 예산을 초과하지 않은 ?
    print(f"mid: {mid}, total: {total}, start: {start}, end: {end}")

        
    #print("================")
    #print(*arr2)
    
    # 멀기준으로 start와 end를 조절할거냐? 
    # 예산을 초과하면 뒤를 땡기고 모지라면 앞을 땡기고 맞나 ?   
    if total <= money :
        
        result = mid
        start = mid + 1
    else :
        end = mid - 1
           
    
   # print("money=", money, ", benefit=", benefit)
print(result)
        
            
        
        
'''
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 

상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다. 
'''
