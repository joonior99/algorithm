// 별 찍기 - 2

// 첫째 줄부터 N번째 줄까지 '오른쪽을 기준으로' 정렬한 별을 차례대로 출력한다

n = int(input())
for i in range(1, n+1):
  print(''*(n-i) + '*'*i)
