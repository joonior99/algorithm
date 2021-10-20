// 좌표 정렬하기 2

// 2차원 평면 위의 점 N개가 주어진다
// 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오
// 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어지고, 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다

n = int(input())
a = []
for i in range(n):
  [x, y] = map(int, input().split())
  reverse = [y, x] // x, y를 뒤집어 [y, x] 형태로 a 리스트에 추가한다
  a.append(reverse)
b = sorted(a)
for i in range(n): // [y, x] 형태로 저장되어 있었기 때문에 다시 출력될 때는 x y 형태로 출력된다
  print(b[i][1], b[i][0])

  
import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
  li.append(list(map(int, sys.stdin.readline().split())))
li.sort(key=lambda x: (x[1], x[0]))
for i in li:
  print(i[0], i[1])
