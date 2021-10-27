// 큰 수의 법칙

// 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다
// 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다
// 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다
// 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오

// 이 문제를 해결하려면 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다
// 연속으로 더할 수 있는 횟수는 최대 K번이므로 '가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산'을 반복하면 된다

n, m, k = map(int, input().split())
data = list(map(int, input().split())) // n개의 수를 공백으로 구분하여 입력받기

data.sort() // 입력받은 수들 정렬하기
first = data[n - 1] // 가장 큰 수
second = data[n - 2] // 두번째로 큰 수

result = 0

while True:
  for i in range(k): // 가장 큰 수를 k번 더하기
    if m == 0: // m이 0이라면 반복문 탈출
      break
    result += first
    m -= 1 // 더할 때마다 1씩 빼기
  if m == 0: // m이 0이라면 반복문 탈출
    break
  result += second // 두 번째로 큰 수를 한 번 더하기
  m -= 1 // 더할 때마다 1씩 빼기
  
print(result)

// M의 크기가 만약 100억 이상처럼 크다면...
// 반복되는 수열에 대해서 파악하면 이 문제를 풀 수 있다
// M을 (K + 1)로 나눈 몫이 수열이 반복되는 횟수가 되고, 여기에서 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다
// M이 (K + 1)로 나누어떨어지지 않는 경우도 고려해야 하는데 '가장 큰 수가 더해지는 횟수'는 int(M / (K + 1)) * K + M % (K + 1) 이다

n, m, k = map(int, input().split())
data = list(map(int, input().split())) // n개의 수를 공백으로 구분하여 입력받기

data.sort() // 입력받은 수들 정렬하기
first = data[n - 1] // 가장 큰 수
second = data[n - 2] // 두번째로 큰 수

count = int(m / (k + 1)) * k // 가장 큰 수가 더해지는 횟수 계산
count += m % (k + 1)

result = 0
result += (count) * first // 가장 큰 수 더하기
result += (m - count) * second // 두번째로 큰 수 더하기

print(result)
