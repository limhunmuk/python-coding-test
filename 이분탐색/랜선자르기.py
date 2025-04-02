cnt, need_count = map(int, input().split())

arr = []
for _ in range(cnt):
    arr.append(int(input()))

# 이분 탐색 범위 설정
start = 1  # 랜선의 최소 길이
end = max(arr)  # 랜선의 최대 길이
result = 0

while start <= end:
    mid = (start + end) // 2  # 랜선을 잘라낼 길이
    total_count = 0

    # 현재 길이(mid)로 잘랐을 때 얻을 수 있는 랜선 개수 계산
    for line in arr:
        total_count += line // mid

    print("start >",start,", end >", end, ",total_count >", total_count, ", need_count >", need_count)
    
    if total_count >= need_count:  # 원하는 개수 이상 만들 수 있다면
        result = mid  # 현재 길이가 최대 길이일 가능성 있음
        start = mid + 1
    else:  # 랜선 개수가 부족하다면 길이를 줄임
        end = mid - 1

print(result)  # 최종적으로 가능한 랜선 최대 길이 출력

#추가 이해가 필요하겠구만
"""
    수정된 코드의 동작
mid는 현재 랜선의 길이입니다.

각 랜선의 길이를 line // mid로 잘라서 얻을 수 있는 랜선 개수를 계산합니다.

조건에 따라:

total_count >= need_count: 랜선을 충분히 만들 수 있으니 더 긴 길이를 탐색.

total_count < need_count: 부족하니 더 짧은 길이를 탐색.

추가 설명
이분 탐색:

이 알고리즘은 start, end, mid를 반복적으로 조정하며 최대 값을 찾는 효율적인 방법입니다.

시간 복잡도:

배열 정렬 없이 가능하며, 대략 O(log(max_length) * cnt) 수준입니다.

테스트:

예를 들어, 랜선이 [400, 300, 500]이고 N = 7인 경우를 테스트해 보세요.

이 코드로 문제를 해결할 수 있을 거예요! 추가 질문이나 궁금한 점 있으면 말씀해주세요. 😊
"""