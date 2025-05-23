# 입력
# 5 
# 출력 
# 11475

# 조건
# 00시 00분 00초 ~ N시 59분 59초까지 모든 시각까지 3이 하나라도 포함되는 모든 경우의 수

h = int(input())

count = 0
for hh in range(h+1):
    for mm in range(60) :
        for ss in range(60):
            print(str(hh)+str(mm)+str(ss))
            if '3' in str(hh)+str(mm)+str(ss):
                count += 1
print(count)