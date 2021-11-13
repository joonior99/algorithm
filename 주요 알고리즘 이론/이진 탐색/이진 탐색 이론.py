// 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다
// 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다
// 이진 탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 시작점, 끝점, 그리고 중간점이다
// 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는게 이진 탐색 과정이다
// 이진 탐색은 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)이다

// 재귀 함수로 구현한 이진 탐색
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2 // 찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  elif array[mid] > target: // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    return binary_search(array, target, start, mid - 1)
  else: // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    return binary_search(array, target, mid + 1, end)
    
n, target = list(map(int, input().split())) // 원소의 개수와 찾고자 하는 문자열 입력받기
array = list(map(int, input().split())) // 전체 원소 입력받기

result = binary_search(array, target, 0, n - 1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result + 1)
  
// 반복문으로 구현한 이진 탐색
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2 // 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    elif array[mid] > target: // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
      end = mid - 1
    else: // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
      start = mid + 1
  return None 

n, target = list(map(int, input().split())) // 원소의 개수와 찾고자 하는 문자열 입력받기
array = list(map(int, input().split())) // 전체 원소 입력받기

result = binary_search(array, target, 0, n - 1)
if result == None:
 print("원소가 존재하지 않습니다.")

else:
  print(result + 1)
  
// 트리 자료구조
// 데이터베이스는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용하여 항상 데이터가 정렬되어 있다
// 트리 자료구조는 노드와 노드의 연결로 표현하며 노드는 정보의 단위로서 어떠한 정보를 가지고 있는 개체로 이해할 수 있다
// 트리 자료구조는 그래프 자료구조의 일종으로 데이터베이스 시스템이나 파일 시스템과 같은 곳에서 많은 양의 데이터를 관리하기 위한 목적으로 사용한다
// 트리는 부모 노드와 자식 노드의 관계로 표현된다
// 트리의 최상단 노드를 루트 노드라고 하며, 트리의 최하단 노드를 단말 노드라고 한다
// 트리에서 일부를 떼어내도 트리 구조이며 이를 서브 트리라고 한다
// 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다

// 이진 탐색 트리
// 트리 자료구조 중에서 가장 간단한 형태가 이진 탐색 트리이다
// 이진 탐색 트리는 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다
// 부모 노드보다 왼쪽 자식 노드가 작으며 부모 노드보다 오른쪽 자식 노드가 크다
// 공식에 따라 루트 노드부터 왼쪽 자식 노드 혹은 오른쪽 자식 노드로 이동하며 반복적으로 방문한다
// 자식 노드가 없을 때까지 원소를 찾지 못했다면, 이진 탐색 트리에 원소가 없는 것이다

// 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다
// 입력 데이터의 개수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있다
// sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다

import sys
input_data = sys.stdin.readline().rstrip()
print(input_data)
