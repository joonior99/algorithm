// 퀵 정렬
// 퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다
// 퀵 정렬에서는 피벗(pivot)이 사용되며 큰 수와 작은 수를 교환할 때 교환하기 위한 '기준'을 피벗이라고 표현한다
// 호어 분할 방식: 리스트에서 첫번째 데이터를 피벗으로 설정한 후 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾고 그 다음 큰 데이터와 작은 데이터의 위치를 서로 교환한다
// 현재 왼쪽에서 찾는 값과 오른쪽에서부터 찾는 값의 위치가 서로 엇갈린 경우 작은 데이터와 피벗의 위치를 서로 변경한다
// 피벗을 기준으로 왼쪽에는 피벗보다 작은 데이터, 오른쪽에는 피벗보다 큰 데이터가 위치하도록 하는 작업을 '분할' 혹은 '파티션'이라고 한다
// 퀵 정렬에서는 특정한 리스트에서 피벗을 설정하여 정렬을 수행한 이후에, 피벗을 기준으로 왼쪽 리스트와 오른쪽 리스트에서 각각 다시 정렬을 수행한다
// 퀵 정렬은 재귀 함수 형태로 작성했을 때 구현이 간결해지는데 이 때 종료 조건은 현재 리스트의 데이터 개수가 1개인 경우이다
// 퀵 정렬의 평균 시간 복잡도는 O(NlogN)이며 선택 정렬, 삽입 정렬에 비해 데이터의 개수가 많을수록 빠르게 동작한다

// 직관적인 형태의 퀵 졍렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: // 원소가 1개인 경우 종료
    return
  pivot = start // 피벗은 첫번째 원소
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]: // 피벗보다 큰 데이터를 찾을 때까지 반복한다
      left += 1
    while right > start and array[right] >= array[pivot]: // 피벗보다 작은 데이터를 찾을 때까지 반복한다
      right -= 1
    if left > right: // 엇갈렸다면 작은 데이터와 피벗을 교체한다
      array[right], array[pivot] = array[pivot], array[right]
    else: // 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체한다
      array[left], array[right] = array[right], array[left]
  // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행한다
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)
  
quick_sort(array, 0, len(array) - 1)
print(array) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

// 파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  if len(array) <= 1: // 리스트가 하나 이하의 원소만을 담고 있다면 종료한다 
    return array
  
  pivot = array[0] // 피벗은 첫번째 원소
  tail = array[1:] // 피벗을 제외한 리스트
  
  left_side = [x for x in tail if x <= pivot] // 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] // 분할된 오른쪽 부분
  
  return quick_sort(left_side) + [pivot] + quick_sort(right_side) // 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환한다

print(quick_sort(array)) // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
