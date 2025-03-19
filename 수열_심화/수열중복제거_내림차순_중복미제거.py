def recur(cnt):
    if cnt == M:  # 길이가 M인 수열을 완성했을 때
        print(*arr)  # 수열 출력
        return

    for i in range(N, 0, -1):  # 내림차순: 큰 숫자부터 작은 숫자로 탐색
        arr.append(i)  # 숫자 추가
        recur(cnt + 1)  # 재귀 호출
        arr.pop()  # 마지막 숫자를 제거하여 백트래킹

# 입력받기
N, M = map(int, input().split())  # N: 숫자 범위, M: 수열 길이
arr = []  # 수열을 저장할 리스트
recur(0)  # 재귀 호출 시작
