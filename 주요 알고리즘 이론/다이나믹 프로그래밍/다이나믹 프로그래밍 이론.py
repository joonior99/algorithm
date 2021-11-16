// 우리는 연산 속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘을 작성해야 한다
// 다이나믹 프로그래밍에서 다이나믹은 '프로그래밍이 실행되는 도중에'라는 의미이다
// 다이나믹 프로그래밍으로 해결할 수 있는 대표적인 예시는 피보나치 수열이 있다
// 피보나치 수열은 이전 두 항의 합을 현재의 항으로 설정하는 특징이 있는 수열이다
// 프로그래밍에서 이러한 수열을 배열이나 리스트로 표현할 수 있으며 수열 자체가 여러 개의 수가 규칙에 따라서 배열된 형태를 의미하는 것이기 때문이다

// 피보나치 함수를 재귀 함수로 구현
// 이렇게 작성하면 f(n) 함수에서 n이 커지면 커질수록 반복해서 호출하는 수가 많아져 수행 시간이 기하급수적으로 늘어나 심각한 문제가 발생할 수 있다
// 피보나치 수열의 시간 복잡도는 O(2^N)이다
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

// 다이나믹 프로그래밍 조건
// 1. 큰 문제를 작은 문제로 나눌 수 있다
// 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다
// 메모이제이션 기법은 다이나믹 프로그래밍을 구현하는 방법의 한 종류로, 한 번 구한 결과를 메모리 공간에 메모해두고(리스트에 저장) 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법을 의미한다
// 메모이제이션은 값을 저장하는 방법이므로 캐싱(caching)이라고도 한다

// 피보나치 수열(재귀적)
// 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

// 피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
  if d[x] != 0: // 이미 계산한 적 있는 문제라면 그대로 반환
    return d[x]
  d[x] = fibo[x - 1] + fibo[x - 2] // 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  return d[x]

print(fibo(99))

// 다이나믹 프로그래밍을 적용했을 때의 피보나치 수열 알고리즘의 시간 복잡도는 O(N)이다
// 그 이유는 f(1)을 구한 다음 그 값이 f(2)를 푸는데 사용되고 f(2)의 값이 f(3)을 푸는데 사용되는 방식으로 이어지기 때문이다
d = [0] * 100

def pibo(x):
  print('f(' + str(x) + ')', end = ' ')
  if x == 1 or x == 2:
    return 1
  if d[x] != 0:
    return d[x]
  d[x] = pibo(x - 1) + pibo(x - 2)
  return d[x]

pibo(6) // f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)

// 재귀 함수를 이용하여 다이나믹 프로그래밍 소스코드를 작성하는 방법을, 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 '탑다운 방식'이라고 한다. 
// 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을 도출한다고 하여 '보텀업 방식'이라고 한다. 
// 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다

// 피보나치 수열을 반복문으로 이용
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1): // 피보나치 함수를 재귀함수로 구현(보텀업 다이나믹 프로그래밍)
  d[i] = d[i - 1] + d[i - 2]
  
print(d[n])
