// N과 M(2)

// 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오
// 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
// 고른 수열은 오름차순이어야 한다
// 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 하고, 수열은 사전 순으로 증가하는 순서로 출력해야 한다

// 문제에서는 [1, 2], [2, 1]과 같은 경우도 중복으로 취급한다

n, m = list(map(int, input().split()))
li = []
def dfs(start):
  if len(li) == m:
    print(''.join(map(str, li)))
    return
    
  for i in range(start, n+1): // [2, 1]과 같이 앞의 숫자가 뒤의 숫자보다 작은 경우를 제외하기위해 start부터 n까지 숫자를 사용한다
    if i not in li:
      li.append(i)
      dfs(i+1) // 재귀함수를 호출할 때는 i를 이용하여 자신의 다음숫자를 부른다
      li.pop()
dfs(1)

// dfs(1) -> i=1, li[1] -> dfs(2) -> i=2, li[1, 2] -> dfs(3) -> m=2 이므로 print(li) -> li.pop(), li[1] -> i=3, li[1, 3] 
