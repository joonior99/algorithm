// 정수 1개 입력받아 그 수까지 출력하기 1

n = int(input())
i = 0

while n>=i:
  print(i)
  i+=1
  
// 정수 1개 입력받아 그 수까지 출력하기 2

n = int(input())
for (i in range(n+1)): // range(n) 은 0, 1, 2, ... , n-2, n-1 까지의 수열을 의미한다
  print(i) 
