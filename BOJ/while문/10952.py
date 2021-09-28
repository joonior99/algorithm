// A+B-5

// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오
// 입력의 마지막에는 0 두 개가 들어온다

while True: // 무한루프로 while문을 돌린다
  a, b = map(int, input().split())
  if (a == 0 and b == 0): // a, b 모두 0이라면 break로 while문을 빠져나온다
    break
  else:
    print(a+b)
