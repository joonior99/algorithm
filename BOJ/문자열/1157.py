// 단어 공부

// 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오
// 단, 대문자와 소문자를 구분하지 않는다
// 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력하고 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다

word = input().upper() // upper 함수를 이용하여 문자열을 모두 대문자로 변환
unique_alphabet = list(set(word)) // 입력받은 문자열에서 중복 값 제거

cnt_list = []
for i in unique_alphabet:
  cnt = word.count(i)
  cnt_list.append(cnt) // count 숫자를 리스트에 append
  
if cnt_list.count(max(cnt_list)) > 1: // count 숫자 최댓값이 중복된다면
  print('?')
else:
  max_index = cnt_list.index(max(cnt_list)) // count 숫자 최댓값 위치
  print(unique_alphabet[max_index])
