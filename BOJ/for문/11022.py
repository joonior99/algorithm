// A+B-8

// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오
// 첫째 줄에 테스트 케이스의 개수 T가 주어진다
// 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력하고 x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다

t = int(input())

for i in range(1, t+1):
  a, b = map(int, input().split())
  c = a+b
  print('Case #%d: %d + %d = %d' %(i, a, b, c))
