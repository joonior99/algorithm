// 네 번째 점

// 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오
// 세 점의 좌표가 한 줄에 하나씩 주어진다

x_nums = []
y_nums = []

for _ in range(3):
  x, y = map(int, input().split())
  x_nums.append(x)
  y_nums.append(y)

for i in range(3): // for 문이 반복되는 동안 count 함수를 이용해서 두 개의 리스트에서 각 인덱스에 위치한 요소의 개수가 한 개인지를 찾았다
  if x_nums.count(x_nums[i]) == 1: 
    x4 = x_nums[i]
  if y_nums.count(y_nums[i]) == 1:
    y4 = y_nums[i]
print(x4, y4)
