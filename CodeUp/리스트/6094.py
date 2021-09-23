// 이상한 출석 번호 부르기 3

// 출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자
// 단, 첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모르고, 음수(-) 번호, 0번 번호도 있을 수 있다

n = int(input()) // 10
a = input().split() // 10 4 2 3 6 6 7 9 8 5

for i in range(n):
  a[i] = int(a[i])

min = a[0]
for i in range(0, n):
  if a[i] < min:
    min = a[i]

print(min)

n = int(input())
print(min(map(int, input().split())))
