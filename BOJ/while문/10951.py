// A+B-4

// 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오

while True:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except:
    break
    
// try - except 구문의 기본적인 구조는 try 구문 쪽에 에러가 발생할 가능성이 있는 코드를 작성하고 except 구문 쪽에 예외 발생 시 실행할 코드를 작성하는 것이다
