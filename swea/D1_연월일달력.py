calendar =[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for test_case in range(1, T + 1):
    data = input().strip()      #날짜데이터를 입력받고 양쪽의 공백 제거
    year = data[:4].zfill(4)        #입력된 날짜에서 연도부분추출하고, 필요한 경우 앞에 0을 채워 4자리로
    month = data[4:6].zfill(2)
    day = data[6:].zfill(2)
    answer = '-1'       #날짜가 유호하지 않을 경우에는 -1

    if(int(year) * int(month) * int(day) == 0) or int(day) > calendar[int(month)]:
        # 입력된 연도,월,일 중에 하나라도 0이거나, 일이 해당월의 일수를 초과하는 경우 유효하지 않은 날짜
        print(f'#{test_case} {answer}')
    else:
        answer = [year, month, day]
        print(f'#{test_case} {"/".join(answer)}')