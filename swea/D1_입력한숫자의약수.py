n = int(input())

for i in range(1, n + 1):       # 1부터 입력한 숫자 n까지
    if n % i == 0:
        print(i, end=' ')