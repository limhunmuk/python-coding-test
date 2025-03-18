def recur(start, in_number, out_text):
    if in_number == M:  # M개를 골랐을 때 출력
        print(out_text.strip())  # 공백 제거 후 출력
        return

    for i in range(start, N + 1):  # start부터 시작해 오름차순 유지
        recur(i + 1, in_number + 1, out_text + str(i) + " ")  # 다음 숫자 선택


# 입력 처리
N, M = map(int, input().split())
recur(1, 0, "")

