// 이상한 출석 번호 부르기 2

// 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자

n = int(input()) // 10
a = input().split() // 10 4 2 3 6 6 7 9 8 5

for i in range(n):
  a[i] = int(a[i])

for i in range(n-1, -1, -1): // n-1, n-2, ..., 3, 2, 1, 0
  print(a[i], end=' ') // 5 8 9 7 6 6 3 2 4 10
