# 1. 필요한 자료구조

### 스택

- FILO
- 별도의 라이브러리 필요 x

```python
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)

print(stack)
print(stack[::-1]) #최상단 원소부터
```

### 큐

- FIFO
- deque 라이브러리 이용 → 큐와 스택의 장점 모두

```python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
print(queue.reverse()) #나중에 들어온 순서대로
```

### 재귀함수

- 내부에서 스택 자료구조 이용

    → 가장 마지막에 호출한 함수가 먼저 끝나야 앞의 함수호출 종류

```python
def factorial_iterative(n):
	result = 1
	for i in range(1, n+1):
		result += i
	return result

def factorial_recursive(n):
	if n <= 1:
		return 1
	return n*factorial_recursive(n-1)
```

# 2. 탐색 알고리즘 DFS/BFS

### 그래프의 표현

1. 인접 행렬 

    : 2차원 배열로 그래프의 연결 관계 표현

    → 연결되지 않은 노드끼리의 비용을 무한대로

    ```python
    INF = 999999999
    graph = [
    	[0, 7, 5],
    	[7, 0, INF],
    	[5, INF, 0]
    ]
    ```

2. 인접 리스트

    : 리스트로 그래프의 연결 관계를 표현하는 방식

    ```python
    graph = [[] for _ in range(3)]

    graph[0].append(1,7)]
    graph[0].append(2,5)]
    graph[1].append(0,7)]
    graph[2].append(0,5)]
    ```

### DFS

- 스택 이용 → **재귀**
- 동작 과정

    : 탐객 시작 노드를 스택에 삽입, 방문 처리 

    → 스택의 최상단 노드에 방문하지 않은 인접노드가 있으면 해당 노드 스택에 넣고 방문, 없으면 스택에서 최상단 노드 pop

    → 2번 과정을 반복

```python
	def dfs(graph, v, visited):
		#현재 노드 방문처리하기
		visitied[v] = True
		print(v, end=' ')
	
		#현재 노드와 연결된 다른 노드를 재귀적으로 방문하기
		for i in graph[v]:
			if not visited[i]:
				dfs(graph, i, visited)

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

visited = [False]*9
dfs(graph, 1, visited)
```

- 장점

    -현 경로상의 노드를 기억하므로 적은 메모리 사용

    -찾으려는 노드가 깊은 단계에 있는 경우 bfs보다 빠름

- 단점

    -얻은 해가 최단 경로라는 보장이 없음 → DFS는 해에 도착하면 탐색 종료함

    -해가 없는 경로에도 끝까지 탐색함

### BFS

- 가까운 노드부터 탐색
- **queue** 이용해서 구현
- 동작과정

    : 탐색 시작 노드를 큐에 삽입, 방문처리

    → 큐에서 노드 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입, 방문처리

    → 2번 과정을 반복

- O(N)

    → 실제 수행 시간이 일반적으로 dfs보다 나음

```python
from collections import deque

	def bfs(graph, start, visited):
		queue = deque([start])
		visited[start] = True
		
		#큐가 빌 때까지 반복
		while queue:
			#큐에서 하나의 원소 뽑아 출력
			v = queue.popleft()
			print(v, end=' ')
			for i in graph[v]:
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

visited = [False]*9
bfs(graph, 1, visited)
```

→ 2차원 배열에서의 탐색 문제는 그래프 형태로 바꿔서 생각하기

- 장점

    -답이 여러개여도 최단경로임을 보장

    -최단경로가 존재하면 깊이가 무한정 깊어져도 찾을 수 있음

- 단점

    -경로가 매우 길 경우 메모리 많이 필요

    -해가 없는 유한 그래프의 경우 모든 그래프 탐색 후 실패로 끝남

    -무한 그래프의 경우 답을 찾지도, 끝내지도 못함

### DFS와 BFS 무엇을 선택해야 할까?

[DFS와 BFS](https://www.notion.so/e34f0cdc3c984fada87a7a816dc89906)

[문제 리스트](https://www.notion.so/f285bd5522cd4cb28bab75ae4bea4137)

[DFS와 BFS](https://www.acmicpc.net/step/24)