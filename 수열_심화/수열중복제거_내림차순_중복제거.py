def recur(start, depth):
    if depth == M:  # 길이가 M인 수열 완성
        print(*result)
        return

    for i in range(start, 0, -1):  # 내림차순 탐색
        if i in result:  # 중복 체크
            continue  # 이미 선택된 숫자는 제외
        result.append(i)  # 숫자 추가
        recur(i - 1, depth + 1)  # 다음 탐색
        result.pop()  # 백트래킹

N, M = map(int, input().split())
result = []
recur(N, 0)
