// 소트인사이드

// 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자
// 첫째 줄에 정렬하려고 하는 수 N이 주어진다

n = int(input())
 
li = []
for i in str(n):
  li.append(int(i)) // li = list(map(int, str(n)))으로 변경 가능하다
    
li.sort(reverse=True) // 내림차순
 
for i in li:
  print(i, end='')
