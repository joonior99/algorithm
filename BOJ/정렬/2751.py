// 수 정렬하기 2

// N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오
// 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다
// 수는 중복되지 않는다

n = int(input())
result = []

for i in range(n):
  result.append(int(input()))

num = sorted(set(result))

for i in num:
  print(i)

// pypy는 python으로 만든 언어이므로 파이썬에서 돌아가면 코드 전환상에는 문제가 없으며, 속도가 더 빠르다는 장점도 있다 
