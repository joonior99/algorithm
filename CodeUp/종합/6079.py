// 언제까지 더해야 할까?

// 1, 2, 3 ... 을 계속 더해 나갈 때, 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만 계속 더하는 프로그램을 작성해보자

n = int(input())
s = 0
t = 0
while s<n:
  t+=1
  s+=t
print(t)
