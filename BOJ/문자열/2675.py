// 문자열 반복

// 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오
// 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다
// 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다

t = int(input())

for _ in range(t):
  cnt, s = input().split()
  for i in s:
    print(i*int(cnt), end='') // end=''는 다음 줄로 넘어가지 않고 그 줄에서 계속 출력하기 위해 사용
  print() // 줄 넘김
