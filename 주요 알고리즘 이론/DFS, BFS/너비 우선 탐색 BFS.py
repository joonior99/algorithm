// BFS는 너비 우선 탐색으로 가까운 노드부터 탐색하는 알고리즘이다
// DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하며 BFS는 그 반대다
// BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용한다
// 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다
// 2. 큐에서 노드를 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다
// 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 방문한다
// BFS는 큐 자료구조에 기초한다는 점에서 구현이 간단하다
// deque 라이브러리를 사용하는 것이 좋으며 탐색 수행에 있어서 O(N)의 시간이 소요된다

from collections import deque

// BFS 메서드 정의
def bfs(graph, start, visited):
  queue = deque([start]) // 큐 구현을 위해 deque 라이브러리 사용
  visited[start] = True // 현재 노드를 방문 처리
  while queue: // 큐가 빌 때까지 반복
    v = queue.popleft() // 큐에서 하나의 원소를 뽑아 출력
    print(v, end='')
    for i in graph[v]: // 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        
graph = [
  [], 
  [2, 3, 8],
  [1, 7], 
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]   

// 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

// 정의된 BFS 함수 호출
 bfs(graph, 1, visited) // 1 2 3 8 7 4 5 6
