// 나머지

// 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다
// 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오

n = set() // 중복되는 요소 제거
for _ in range(10):
  i = int(input())
  n.add(i%42) // 집합 자료형에 원소를 추가할 때 add 함수를 사용
print(len(n))
