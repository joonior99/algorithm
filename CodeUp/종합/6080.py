// 주사위 2개 던지기

// 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때, 나올 수 있는 모든 경우를 출력해보자
// 바깥쪽의 i 값이 1부터 n까지 순서대로 바뀌는 각각의 동안에 안쪽의 j 값이 다시 1부터 m까지 변하며 출력되는 코드이다

n, m = input().split()
n = int(n)
m = int(m)
for i in range(1, n+1):
  for j in range(1, m+1):
    print(i, j)
