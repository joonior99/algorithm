// 터렛

// 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고, 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오
// 첫째 줄에 테스트 케이스의 개수 T가 주어진다
// 한 줄에 x1, y1, r1, x2, y2, r2가 주어진다
// 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다

import math

t = int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distance = math.sqrt((x1-x2)**2 + (y1-y2)**2) // 두 터렛 사이의 거리를 반지름으로 하는 원이 있다고 할 때 원의 방정식을 활용한 식
  if distance == 0 and r1 == r2: // 두 원이 동심원이며 반지름이 같을 때의 식을 의미
    print(-1)
  elif abs(r1-r2) == distance or r1+r2 == distance: // 두 원이 내접 혹은 외접할 때의 식을 의미
    print(1)
  elif abs(r1-r2) < distance < (r1+r2): // 두 원이 서로 다른 두 점에서 만날 때의 식을 의미
    print(2)
  else:
    print(0) 
