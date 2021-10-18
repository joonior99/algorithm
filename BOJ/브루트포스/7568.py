// 덩치

// 우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다
// 어떤 사람의 몸무게가 x kg이고 키가 y cm라면 이 사람의 덩치는 (x, y)로 표시된다
// N명의 집단에서 각 사람의 덩치 등수는 자신보다 더 "큰 덩치"의 사람의 수로 정해지고 만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다
// 이렇게 등수를 결정하면 같은 덩치 등수를 가진 사람은 여러 명도 가능하다
// 여러분은 학생 N명의 몸무게와 키가 담긴 입력을 읽어서 각 사람의 덩치 등수를 계산하여 출력해야 한다
// 첫 줄에는 전체 사람의 수 N이 주어지고, 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다

n = int(input())
student_list = []

for _ in range(n):
  x, y = map(int, input().split())
  student_list.append((x, y))

for i in student_list:
  rank = 1
  for j in student_list:
    if i[0] < j[0] and i[1] < j[1]: // i[0], i[1]은 몸무게 비교, j[0], j[1]은 키 비교
      rank += 1
  print(rank, end = " ")
