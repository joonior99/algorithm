// 부품 찾기

// 전자 매장에는 부품이 N개 있으며 각 부품은 정수 형태의 고유한 번호가 있다
// 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다
// 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 하는데 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자
// 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes, 없으면 no를 출력하고 구분은 공백으로 한다
// 첫째 줄에 정수 N이 주어지고(1 <= N <= 1,000,000) 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다
// 셋째 줄에 정수 M이 주어지고(1 <= N <= 100,000) 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다

// 이진 탐색 알고리즘을 이용한 방법
// 먼저 매장 내 N개의 부품을 번호 기준으로 정렬하고 그 이후에 M개의 찾고자 하는 부품이 각각 매장에 존재하는지 검사하면 된다
// 이때 이진 탐색을 사용한 시간 복잡도는 O((M + N) x logN)이다

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target: // 찾은 경우 중간점 인덱스 반환
      return mid
    elif array[mid] > target: // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
      end = mid - 1
    else: // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
      start = mid + 1
  return None

n = int(input())
array = list(map(int, input().split())) // 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array.sort() // 이진 탐색을 수행하기 위해 사전에 정렬 수행
m = int(input())
x = list(map(int, input().split()))

for i in x: // 손님이 확인 요청한 부품 번호를 하나씩 확인
  result = binary_search(array, i, 0, n - 1) // 해당 부품이 존재하는지 확인
  if result != None:
    print('yes', end=' ')
  else:
    print('no', end=' ')


// 계수 정렬의 개념을 이용한 방법
// 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤에, 리스트의 인덱스에 직접 접근하여 특정한 번호의 부품이 매장에 존재하는지 확인한다

n = int(input())
array = [0] * 1000001

for i in input().split(): // 가게에 있는 전체 부품 번호를 입력받아서 기록
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split())) // 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

for i in x: // 손님이 확인 요청한 부품 번호를 하나씩 확인
  if array[i] == 1:
    print('yes', end=' ')
  else:
    print('no, end=' ')
          
          
// 집합 자료형을 이용한 방법
// 단순히 특정한 수가 한 번이라도 등장했는지를 검사하면 되므로 집합 자료형을 이용하여 문제를 해결할 수 있다

n = int(input())
array = set(map(int, input().split())) // 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
m = int(input())
x = list(map(int, input().split())) // 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력

for i in x: // 손님이 확인 요청한 부품 번호를 하나씩 확인
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
