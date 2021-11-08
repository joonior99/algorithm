// 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열한 것을 의미한다
// 정렬 알고리즘으로 데이터를 정렬하면 이진 탐색(Binary Search)이 가능해진다

// 선택 정렬
// '가장 작은 것을 선택'해서 앞으로 보내는 과정을 반복해서 수행하다 보면, 전체 데이터의 정렬이 이루어진다
// 선택 정렬은 가장 작은 데이터를 앞으로 보내는 과정을 N - 1 번 반복하면 정렬이 완료된다
// 선택 정렬의 시간 복잡도는 O(N^2)이며 소스코드 상으로 간단한 형태의 2중 반복문이 사용되었기 때문이다
// 선택 정렬은 기본 정렬 라이브러리를 포함하여 데이터 개수를 증가시킬 때 속도가 급격히 느려져 다른 알고리즘과 비교했을 때 매우 비효율적이다
// 특정한 리스트에서 가장 작은 데이터를 찾은 일이 코딩 테스트에서 잦으므로 선택 정렬 소스코드 형태에 익숙해져야 한다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i // 가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] // 스와프(특정한 리스트가 주어질 때 두 변수의 위치를 변경하는 작업)
  
print(array) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

// 스와프
array = [3, 5]
array[0], array[1] = array[1], array[0]

print(array) // [5, 3]

// 삽입 정렬
// 선택 정렬에 비해 구현 난이도가 높은 편이지만 선택 정렬에 비해 실행 시간 측면에서 더 효율적인 알고리즘이다
// 삽입 정렬은 특정한 데이터를 적절한 위치에 삽입하며, 특정한 데이터가 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정한다
// 삽입 정렬은 두번째 데이터부터 시작하며 그 이유는 첫번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때문이다
// 삽입 정렬에서 정렬이 이루어지는 원소는 항상 오름차순을 유지하고 있다는 특징이 있다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  for j in range(i, 0, -1): // 인덱스 i부터 1까지 감소하며 반복하는 문법
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j]
    else: // 자신보다 작은 데이터를 만나면 그 위치에서 멈춘다
      break
      
print(array) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
