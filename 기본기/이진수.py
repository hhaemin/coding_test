T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]       # bin은 10진수를 2진수로 (0b,,,이런식으로 출력되므로) [2:]
    for i in range(len(n)):
        if n[-i-1] == '1':      # 2진수는 역순으로 읽기 때문에 -i-1
            print(i, end=' ')