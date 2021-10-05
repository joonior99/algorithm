// OX퀴즈

// 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다
// "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다
// OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오

n = int(input())

for _ in range(n):
  ox_list = list(input())
  score = 0
  sum_score = 0 // 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다
  for ox in ox_list: // O이나 X를 하나씩 꺼내서 
    if ox == 'O':
      score += 1 // 'O'가 연속되면 점수가 1점씩 커진다
      sum_score += score 
    else:
      score = 0
  print(sum_score)
