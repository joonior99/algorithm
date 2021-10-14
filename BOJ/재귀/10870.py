// 피보나치 수 5 

// 피보나치 수는 0과 1로 시작하며, 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다
// 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다
// 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다
// n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오

n = int(input())

fibonacci = [0, 1]
for i in range(2, n+1):
  num = fibonacci[i-1] + fibonacci[i-2]
  fibonacci.append(num)
print(fibonacci[n])


def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
