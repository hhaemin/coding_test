n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()      #입력받은 정수 리스트를 오름차순으로 정렬
print(numbers[n // 2])