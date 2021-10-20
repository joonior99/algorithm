// 통계학

// 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있으며 단, N은 홀수라고 가정하자
// 산술평균 : N개의 수들의 합을 N으로 나눈 값, 소수점 이하 첫째 자리에서 반올림한 값을 출력한다
// 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
// 최빈값 : N개의 수들 중 가장 많이 나타나는 값, 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다
// 범위 : N개의 수들 중 최댓값과 최솟값의 차이
// N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오

import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for _ in range(n):
  li.append(int(sys.stdin.readline()))
 
print(round(sum(li)/n)) // 산술평균 
 
li.sort()
print(li[n//2]) // 중앙값
 
cnt_li = Counter(li).most_common() // Counter 자료형은 기본적으로 딕셔너리이며 most_common()는 등장한 횟수를 내림차순으로 정리해서 보여준다
if len(cnt_li) > 1 and cnt_li[0][1]==cnt_li[1][1]: // 최빈값 2개 이상 두번째로 작은 값, e.g. [('a', 2), ('b', 2), ('c', 1)]
  print(cnt_li[1][0])
else:
  print(cnt_li[0][0]) // 최빈값이 1개일 때
 
print(max(li)-min(li)) // 범위
