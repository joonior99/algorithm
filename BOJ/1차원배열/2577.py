// 숫자의 개수

// 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오

a, b, c = map(int, input().split())
total_str = str(a*b*c) // 숫자를 곱하여 str타입으로 변환
for i in range(10):
  num_count = total_str.count(str(i)) // 각 자리의 숫자가 total_str 문자열 안에서 몇 번씩 쓰였는지
  print(num_count)

total = 1
for _ in range(3):
  i = int(input())
  total *= i // 3개의 정수를 곱함
total_str = str(total) // 숫자를 곱하여 str타입으로 변환
for i in range(10):
  num_count = total_str.count(str(i))
  print(num_count)
