// 평균

// 세준이는 자기 점수 중에 최댓값을 골랐고 이 값을 M이라고 한다
// 그리고 나서 모든 점수를 '점수/M*100'으로 고쳤다
// 첫째 줄에 시험 본 과목의 개수 N이 주어진다
// 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오

n = int(input())
test_score = list(map(int, input().split()))
max_score = max(test_score)

new_list = []
for i in test_score:
  new_list.append(i/max_score * 100) // 새로운 점수 
test_avg = sum(new_list)/n // 새로운 평균
print(test_avg)
