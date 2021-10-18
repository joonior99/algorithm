// 수 정렬하기

// N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오
// 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다
// 수는 중복되지 않는다

n = int(input())
result = list()

for i in range(n):
  result.append(int(input()))
  result.sort()
for i in result:
print(i)

// 버블 정렬로 정렬하기

n = int(input())
result = []

for i in range(n):
  result.append(int(input()))

for i in range(len(result)): // 버블 정렬
  for j in range(len(result)):
    if result[i] < result[j]:
      result[i], result[j] = result[j], result[i]
      
for k in result:
  print(k)
