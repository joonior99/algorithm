// 위에서 아래로

// 하나의 수열에는 다양한 수가 존재한다
// 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다
// 수열을 내림차순으로 정렬하는 프로그램을 만드시오
// 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다

n = int(input())

array = []
for i in range(n):
  array.append(int(input()))
  
array = sorted(array, reverse=True) // 파이썬 기본 정렬 라이브러리를 이용하여 정렬 수행

for i in array: 
  print(i, end=' ') // 정렬이 수행된 결과를 공백으로 구분하여 출력
