// 셀프 넘버

// 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자
// 예를 들어, d(75) = 75+7+5 = 87이다
// 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다
// n을 d(n)의 생성자라고 한다
// 생성자가 없는 숫자를 셀프 넘버라고 한다
// 10000보다 작거나 같은 '셀프 넘버'를 한 줄에 하나씩 출력하는 프로그램을 작성하시오

numbers = set(range(1, 10000))
remove_set = set() // 생성자가 있는 숫자의 집합
for num in numbers:
  for i in str(num): // 각 자리수를 분리하기 위하여 str 함수 이용
    num += int(i) // 각 자리수를 합한 수
  remove_set.add(num) 
  
self_numbers = numbers - remove_set // 집합의 '-'연산자는 차집합을 구할 때 사용
for self_num in sorted(self_numbers): // sorted 함수로 정렬
  print(self_num)
