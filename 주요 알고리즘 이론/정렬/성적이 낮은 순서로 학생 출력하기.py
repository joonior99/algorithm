// 성적이 낮은 순서로 학생 출력하기

// N명의 학생 정보가 있다
// 학생 정보는 학생의 이름과 학생의 성적으로 구분된다
// 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오
// 첫번째 줄에 학생의 수 N이 입력된다 (1 <= N <= 100,000)

// 이 문제에서는 학생의 정보가 최대 100,000개 까지 입력될 수 있으므로 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용하거나 O(N)을 보장하는 계수 정렬을 이용해야 한다
// 학생 정보를 (점수, 이름)으로 묶은 뒤에 점수를 기준으로 정렬을 수행해야 한다

n = int(input())

array = []
for i in range(n):
  input_data = input().split()
  array.append((input_data[0], int(input_data[1]))) // 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
  
array = sorted(array, key=lambda student: student[1]) // key를 이용하여, 점수를 기준으로 정렬
for student in array:
  print(student[0], end=' ') 
