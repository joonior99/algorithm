// 소인수분해

// 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오

n = int(input())

if n == 1:
  print('')

for i in range(2, n+1): // 2부터 하나씩 나눠보기
  if n%i == 0: // 숫자가 나눠질 수 있는지 
    while n%i == 0: // 해당 숫자로 나눌 수 없을 때까지 나누기
      print(i)
      n = n/i
