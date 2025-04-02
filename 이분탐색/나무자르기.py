n, m = map(int, input().split())
forest = list(map(int, input().split()))

s=1
e=max(forest)

while s<=e :
    mid=(s+e)//2
    
    wood = 0
    for tree in forest :
        if tree >= mid :
            wood += tree - mid

    if wood >= m : # m은 구하려는 나무길이 - 잘려 나오는 총 나무 길이(wood)는 절단 높이(mid)와 반비례 관계에 있습니다.
        s = mid + 1 # 절단 높이를 높이면(start = mid + 1), 목재 길이가 감소합니다.
    else :
        e = mid - 1 # 절단 높이를 낮추면(end = mid - 1), 목재 길이가 증가합니다.
print(e) # ???
        # 내가 필요한 만큼만 나무를 얻기 위한 높이를 계산해주세요.
        # 문해력이 내가 떨어지나 .. 먼소리냐
        # tree - mid를 뺀값을 wood에 저장하고
        # wood 에 쌓인 값을 이분검색 mid와 비교하여 start += 1 하거나 end -= 1시켜서
        # 만족하는 최종 end값을 리턴한다 (왜 ? -> e값이 가져가려는 두번째 파라미터에 최소절단할 높이가 되기 때문)


