// 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다
// 단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다
// 1. N에서 1을 뺀다
// 2. N을 K로 나눈다
// N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성하시오

// 주어진 N에 대하여 '최대한 많이 나누기'를 수행하면 된다
// 어떠한 수가 있을 때, '2 이상의 수로 나누는 것'이 '1을 빼는 것'보다 숫자를 많이 줄일 수 있기 때문이다
// K가 2 이상이기만 하면 K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N의 값을 줄일 수 있으며, N이 결국 1에 도달한다

n, k = map(int, input().split())
result = 0

while n >= k: // n이 k 이상이라면 k로 계속 나누기
  while n % k != 0: // n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    n -= 1
    result += 1
  n //= k
  result += 1
  
while n > 1: // 마지막으로 남은 수에 대하여 1씩 빼기
  n -= 1
  result += 1

print(result)


n, k = map(int, input().split())
result = 0

while True:
  target = (n // k) * k // (n == k로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
  result += (n - target)
  n = target
  if n < k: // n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    break
  result += 1
  n //= k // k로 나누기
  
result += (n - 1) // 마지막으로 남은 수에 대하여 1씩 빼기
print(result)
