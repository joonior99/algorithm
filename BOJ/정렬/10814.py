// 나이순 정렬

// 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다
// 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오
// 첫째 줄에 온라인 저지 회원의 수 N이 주어지고, 입력은 가입한 순서로 주어진다

import sys
n = int(sys.stdin.readline())
arr = []
 
for _ in range(n):
  arr.append(sys.stdin.readline().split())
 
arr.sort(key=lambda x: int(x[0]))
 
for age, name in arr:
  print(age, name)
