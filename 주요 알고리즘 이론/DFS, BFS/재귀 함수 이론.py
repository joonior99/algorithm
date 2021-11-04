// 재귀함수는 자기 자신을 호출하는 함수를 의미한다

def recursive_function():
  print('재귀 함수를 호출합니다.')
  recursive_function()

recursive_function() // RecursionError: maximum recursion depth exceeded while pickling an object
  
// 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수가 언제 끝날지, if문을 이용하여 종료 조건을 꼭 명시해야 한다
// 재귀 함수의 수행은 스택 자료구조를 이용하는데 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 마쳐야 그 앞의 함수 호출이 종료되기 때문이다
def recursive_function(i):
  if i == 100: // 100번째 출력했을 때 종료되도록 종료 조건 명시
    return
  print(i, '번째 재귀 함수에서', i + 1, '번째 재귀 함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

// 2가지 방식으로 구현한 팩토리얼 
def factorial_iterative(n): // 반복적으로 구현한 n!
  result = 1
  for i in range(1, n + 1): // 1부터 n까지의 수를 차례대로 곱하기
    result *= i
  return result

def factorial_recursive(n): // 재귀적으로 구현한 n!
  if n <= 1: // n이 1 이하인 경우 1을 반환
    return 1
  return n * factorial_recursive(n - 1) // n! = n * (n - 1)!

print(factorial_iterative(5)) // 120
print(factorial_recursive(5)) // 120

