// 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다
// 1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있으며, N은 행의 개수, M은 열의 개수를 의미한다
// 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다
// 3. 그 다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
// 4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다
// 각 숫자는 1 이상 10,000 이하의 자연수이다
// 카드들이 N X M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오

// '각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수'를 찾는 것이다
// 단순히 배열에서 가장 작은 수를 찾는 기본 문법을 이용하여 각 행에서 가장 작은 수를 찾은 다음 그 수 중에서 가장 큰 수를 찾는 방식으로 문제를 해결할 수 있다

n, m = map(int, input().split())

result = 0

for i in range(n): // 한 줄씩 입력받아 확인
  data = list(map(int, input().split()))
  min_value = min(data) // 현재 줄에서 '가장 작은 수' 찾기
  result = max(result, min_value) // '가장 작은 수'들 중에서 가장 큰 수 찾기

print(result)

n, m = map(int, input().split())

result = 0

for i in range(n): // 한 줄씩 입력받아 확인
  data = list(map(int, input().split()))
  min_value = 10001 
  for a in data:
    min_value = min(min_value, a) // 현재 줄에서 '가장 작은 수' 찾기
    result = max(result, min_value) // '가장 작은 수'들 중에서 가장 큰 수 찾기
    
print(result)
