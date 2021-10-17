// 영화감독 숌 

// 영화감독 숌은 세상의 종말 이라는 시리즈 영화의 감독이다
// 조지 루카스는 스타워즈를 만들 때, 스타워즈 1, 스타워즈 2, 스타워즈 3, 스타워즈 4, 스타워즈 5, 스타워즈 6과 같이 이름을 지었고, 피터 잭슨은 반지의 제왕을 만들 때, 반지의 제왕 1, 반지의 제왕 2, 반지의 제왕 3과 같이 영화 제목을 지었다
// 하지만 숌은 자신이 조지 루카스와 피터 잭슨을 뛰어넘는다는 것을 보여주기 위해서 영화 제목을 좀 다르게 만들기로 했다
// 숌은 첫 번째 영화의 제목은 세상의 종말 666, 두 번째 영화의 제목은 세상의 종말 1666 이렇게 이름을 지을 것이다
// 일반화해서 생각하면, N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다
// 숌이 만든 N번째 영화의 제목에 들어간 숫자를 출력하는 프로그램을 작성하시오 
// 숌은 이 시리즈를 항상 차례대로 만들고, 다른 영화는 만들지 않는다

n = int(input())
nth = 666
count = 0

while True:
  if '666' in str(nth): // 666에 관해 str 함수를 이용하여 문자열로 변경하고 666이 포함되어 있다면 카운트 1개 올리는 것이다  
    count += 1              
  if count == n: // 두 번째 if 문에서 count와 N번째 수가 같다면 nth를 출력하고 while 문을 종료시키고 666이 연속으로 포함되어 있는 수가 나올 때까지 nth를 1씩 증가시킨다
    print(nth)           
    break               
  nth += 1    
  
// 1부터 하나씩 추가하여 모든 수를 대입해보는 만큼 정확도는 높지만 긴 시간과 높은 비용이 발생한다  
