// A+B-7

// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오
// 첫째 줄에 테스트 케이스의 개수 T가 주어진다
// 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력하고 테스트 케이스 번호는 1부터 시작한다

t = int(input())

for i in range(1, t+1):
  a, b = map(int, input().split())
  print('Case #%d: %d' %(i, a+b))
