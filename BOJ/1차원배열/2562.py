// 최댓값

// 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오

n = []
for _ in range(9):
  i = int(input())
  n.append(i)
print(max(n))
print(n.index(max(n))+1) // index 함수로 위치를 찾고 1을 더한다

n = []
for i in range(9):
  n.append(int(input())
print(max(n))
print(n.index(max(n))+1)
