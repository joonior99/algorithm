// 두 수 비교하기

// A가 B보다 큰 경우에는 '>'를 출력한다
// A가 B보다 작은 경우에는 '<'를 출력한다
// A와 B가 같은 경우에는 '=='를 출력한다

A, B = map(int, input().split())
if A > B:
  print('>')
elif A < B:
  print('<')
else:
  print('==')
  
A, B = map(int, input().split())
print('>') if A > B else print('<') if A < B else print('==')
// 삼항 연산자 코드로 작성
