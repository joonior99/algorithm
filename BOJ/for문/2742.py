// 기찍 N

// 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오

n = int(input())
for i in range(n, 0, -1): // 두번째 인자값인 종료값은 해당값을 포함하지 않기 때문에 0을 넣어준다
  print(i)
  
n = int(input())
for i in range(n):
  print(n-i)
