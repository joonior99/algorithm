// 게임 개발

// 캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 N X M 크기의 직사각형으로, 캐릭터는 동서남북 중 한 곳을 바라본다
// 맵의 각 칸은 (A, B)로 나타낼 수 있고 A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다
// 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다
// 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다
// 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다
// 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다
// 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다
// 메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오
// 첫째 줄에 맵의 세로 크기 N, 가로 크기 M을 공백으로 구분하여 입력한다
// 둘째 줄에 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다
// 방향 d의 값은 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
// 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다, 0: 육지, 1: 바다, 맵의 외곽은 항상 바다로 되어 있다

// 전형적인 시뮬레이션 문제이다
// 일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다
// 현재 캐릭터가 북쪽을 바라보고 있을 때는 북쪽으로 이동하기 위해 x와 y좌표를 각각 dx[0], dy[0]만큼 더하며 즉, 현재 위치에서 (-1, 0)만큼 이동시키는 것이다
// 파이썬에서 2차원 리스트를 선언할 때는 컴프리헨션을 이용하는 것이 효율적이다

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)] // 방문한 위치를 저장하기 위한 맵을 생성하여 0을 초기화
x, y, direction = map(int, input().split()) // 현재 캐릭터의 x좌표, y좌표, 방향을 입력받기
d[x][y] = 1 // 현재 좌표 방문 처리

array = [] // 전체 맵 정보를 입력받기
for i in range(n):
  array.append(list(map(int, input().split())))

// 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(): // 왼쪽으로 회전
  global direction // 정수형 변수인 direction 변수가 함수 바깥에서 선언된 전역변수이기 때문에 global 키워드 사용
  direction -= 1
  if direction == -1:
    direction = 3
    
// 시뮬레이션 시작    
count = 0
turn_time = 0
while True:
  turn_left() // 왼쪽으로 회전
  nx = x + dx[direction]
  ny = y + dy[direction]
  if d[nx][ny] == 0 and array[nx][ny] == 0: // 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    d[nx][ny] = 1
    x = nx
    y = ny
    count += 1
    turn_time = 0
    continue
  else: // 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    turn_time += 1
  if turn_time == 4: // 네 방향 모두 갈 수 없는 경우
    nx = x - dx[direction]
    ny = y - dy[direction]
    if array[nx][ny] == 0: // 뒤로 갈 수 있다면 이동하기
      x = nx
      y = ny
    else: // 뒤가 바다로 막혀있는 경우
      break
    turn_time = 0
    
print(count)
  
