// 좌표 정렬하기

// 2차원 평면 위의 점 N개가 주어진다
// 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오
// 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어지고, 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다

n = int(input()) 
nums = [] 
for i in range(n): 
  [a, b] = map(int, input().split()) 
  nums.append([a, b]) 

nums = sorted(nums) 
for i in range(n): 
  print(nums[i][0], nums[i][1]) // pypy3으로 제출


import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
  x, y = map(int, sys.stdin.readline().split())
  li.append([x, y])
li.sort(key=lambda x: (x[0], x[1])) // x좌표 정렬 후 y좌표 정렬
  print(li[i][0], li[i][1])
