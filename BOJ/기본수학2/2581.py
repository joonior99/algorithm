// 소수

// 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오
// 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다

m = int(input())
n = int(input())

prime_list = []
for num in range(m, n+1):
  error = 0
    if num > 1:
      for i in range(2, num):  // 2부터 num-1까지
        if num%i == 0:
          error += 1
          break  // 2부터 num-1까지 나눈 몫이 0이면 error가 증가하고 for문을 종료한다
        if error == 0:
          prime_list.append(num) 
            
if len(prime_list) > 0:
  print(sum(prime_list))
  print(min(prime_list))
else:
  print(-1)
