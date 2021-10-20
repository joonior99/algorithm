// 단어 정렬

// 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오
// 1. 길이가 짧은 것부터 2. 길이가 같으면 사전 순으로
// 첫째 줄에 단어의 개수 N이 주어진다
// 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다

n = int(input())
words_list = []

for _ in range(n):
  word = str(input())
  word_count = len(word)
  words_list.append((word, word_count))

words_list = list(set(words_list)) // 중복 제거
words_list.sort(key=lambda word: (word[1], word[0])) // 단어 숫자 정렬 > 단어 알파벳 정렬

for word in words_list:
  print(word[0])
