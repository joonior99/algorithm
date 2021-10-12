// 소수 찾기

// 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오
// 첫 줄에 수의 개수 N이 주어지고 N은 100이하이다

n = int(input())

numbers = map(int, input().split())
prime = 0
for num in numbers:
  error = 0
  if num > 1:
    for i in range(2, num):  
      if num%i == 0:
        error += 1  // 2부터 n-1까지 나눈 몫이 0이면 error가 증가
    if error == 0:
      prime += 1  // error가 없으면 소수
      
print(prime)
