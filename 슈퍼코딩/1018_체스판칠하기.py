n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())

ans = 64

for s_x in range(n-7):
    for s_y in range(m-7):
        white = 0
        black = 0
        for x in range(8):
            for y in range(8):
                if (x + y) % 2:
                    if board[s_x + x][s_y + y] == "W":
                        black += 1
                    else:
                        white += 1

                else:
                    if board[s_x + x][s_y + y] == "W":
                        white += 1
                    else:
                        black += 1
        ans = min(ans, black, white)
print(ans)