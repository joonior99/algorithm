// 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정을 의미하며 프로그래밍에서는 그래프, 트리 등의 자료구조 안에서 탐색을 하는 문제를 다룬다
// 대표적인 탐색 알고리즘으로 DFS와 BFS를 꼽을 수 있으며 이를 이해하려면 기본 자료구조인 스택과 큐에 대한 이해가 전제되어야 한다
// 자료구조란 데이터를 표현하고 관리하고 처리하기 위한 구조를 의미한다
// 스택은 선입후출(First In Last Out) 구조 또는 후입선출(Last In First Out) 구조라고 할 수 있다
// append() 메서드는 리스트의 가장 뒤쪽에 데이터를 삽입하고, pop() 메서드는 리스트의 가장 뒤쪽에서 데이터를 꺼낸다

stack = []

// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4)- 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) // 최하단 원소부터 출력 [5, 2, 3, 1]
print(stack[::-1]) // 최상단 원소부터 출력 [1, 3, 2, 5]

// 큐는 선입선출(First In First Out) 구조라고 할 수 있다

from collections import deque
// 큐를 구현하기 위한 deque 라이브러리 사용
queue = deque()

// 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4)- 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) // 먼저 들어온 순서대로 출력 deque([3, 7, 1, 4])
queue.reverse() 
print(queue) // 나중에 들어온 원소부터 출력 deque([4, 1, 7, 3])
print(list(queue)) // [4, 1, 7, 3]
