// 바둑알 십자 뒤집기

// 십자 뒤집기는 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다
// 어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다
// 바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자

d=[]
for i in range(20):
  d.append([])
  for j in range(20): 
    d[i].append(0) // 비어있는 리스트에 20개의 리스트를 만들고 각 리스트에 0을 넣는다

for i in range(19): // i = 0 ~ 18
  a = input().split() // 0 0 ... 1 0 1 0 ... 0 0
  for j in range(19): // j = 0 ~ 18
    d[i+1][j+1] = int(a[j])

n = int(input()) // 뒤집는 횟수
for i in range(n):
  x, y = input().split()
  x = int(x)
  y = int(y)
  for j in range(1, 20):
    if d[j][y]==0: // 세로줄 뒤집는다
      d[j][y]=1
    else:
      d[j][y]=0 // 그대로 둔다

    if d[x][j]==0: // 가로줄 뒤집는다
      d[x][j]=1
    else:
      d[x][j]=0

for i in range(1, 20):
  for j in range(1, 20):
    print(d[i][j], end=' ')
  print() // 19*19로 출력하기 위하여 필요하다
