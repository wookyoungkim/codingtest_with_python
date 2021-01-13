# 다익스트라 최단 경로 알고리즘

: 한 노드에서 다른 노드로 가는 **각각의 최단경로** 구하기

## 특징

- 그리디로 분류된다.
    → 매번 **가장 비용이 적은 노드** 선택

- 최단 거리 테이블 : 각 노드에 대한 현재까지의 최단 거리 정보 저장 → 계속 갱신

## 동작 원리

"**방문하지 않은 노드 중 최단거리가 가장 짧은 노드 선택**"을 반복하기

### 초기 상태
![](https://images.velog.io/images/woo0_hooo/post/5d610451-9997-49aa-bc3a-84550590122f/IMG_AE8F108DBA31-1.jpeg)

출발 노드 : 1
![](https://images.velog.io/images/woo0_hooo/post/21326b67-e495-43c2-b7f2-48821d93f4f8/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.48.27.png)

→ 모든 최단 거리를 **무한**(1e9)으로 초기화

### Step 0 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택

→ 출발노드~출발노드는 0이므로 **1번 노드** 선택
![](https://images.velog.io/images/woo0_hooo/post/40019d90-8aac-405f-a569-a50a63a2344d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.49.37.png)

### **Step 1 현재 노드에서 다른 노드로 가는 비용 계산**

현재 노드인 **1번 노드**를 거쳐 다른 노드로 가는 비용 계산
![](https://images.velog.io/images/woo0_hooo/post/148f2ad1-d136-435c-be7d-82f8612db958/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.49.03.png)

### S**tep 2** 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 → 4번 노드
![](https://images.velog.io/images/woo0_hooo/post/10d54fe8-2a7e-4586-b92c-91e4708dbf55/IMG_F2183CACC4C0-1.jpeg)

**4번 노드**를 거쳐 다른 노드로 가는 비용 계산
![](https://images.velog.io/images/woo0_hooo/post/4cd485f5-2dd0-48d0-91a2-ef4c74d5b7b5/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.50.09.png)

### S**tep 3** 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 → 2번 노드
![](https://images.velog.io/images/woo0_hooo/post/f3504e8e-f9ac-47ec-b99a-302dfca49a89/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.51.24.png)

### S**tep 4** 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 → 5번 노드
![](https://images.velog.io/images/woo0_hooo/post/8bb3a27f-ff62-4c2a-9443-2b184c8b6cf5/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.51.41.png)


### S**tep 5** 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 → 3번 노드
![](https://images.velog.io/images/woo0_hooo/post/40cfc681-1717-4ee0-bd8d-fde09d55733b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.51.59.png)

### S**tep 6** 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택 → 6번 노드
![](https://images.velog.io/images/woo0_hooo/post/86e2db80-cd31-49ea-a74b-d1fd03563614/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-01-13%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%202.52.13.png)

→ 최종 최단 거리 테이블

: 1번 노드에서 출발했을때, 2번까지 2, 3번까지 3, 4번까지 1, 5번까지 2, 6번까지 4라는 의미

## 구현

### 방법 1) 간단한 다익스트라 알고리즘

- 매번 방문하지 않은 노드 중 최단거리가 가장 짧은 노드 탐색하기 위해 최단 거리 리스트 **순차 탐색**
- 시간 복잡도 : $O(V^2)$ → V는 노드의 개수
    → 일반적으로 전체 노드의 개수가 **5000개 이하일때만** 사용 가능

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input()) #시작 노드
graph = [[] for _ in range(n+1)] #노드 연결 정보
visited = [False]*(n+1) #방문 여부 체크 배열
distance = [INF]*(n+1) #최단 거리 테이블

for _ in range(m):
    a,b,c = map(int, input().split()) #a->b의 비용 c
    graph[a].append((b,c))

#방문하지 않은 노드 중, 최단거리가 가장 짧은 노드 찾기
def get_smallest_node():
    min_val = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    #시작 노드 처리
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(1, n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```

### 방법 2) 개선된 다익스트라 알고리즘

- **가장 최단거리가 짧은 노드**를 선형적으로 찾는게 아닌 **Heap**을 이용해서 처리

→ 우선순위 큐에 더 짧은 경로를 찾은 노드 넣고, 꺼낼때는 해당 노드를 방문한 적이 있으면 무시, 아니면 처리해주면 된다. 

- 시간 복잡도 : $O(ElogV)$ → V는 노드의 개수, E는 간선의 개수

→ Heap이란? [[Python] Heap](https://velog.io/@woo0_hooo/Python-Heap)을 참고

```python
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input()) #시작 노드
graph = [[] for _ in range(n+1)] #노드 연결 정보
distance = [INF]*(n+1) #최단 거리 테이블

for _ in range(m):
    a,b,c = map(int, input().split()) #a->b의 비용 c
    graph[a].append((b,c))

def dijkstra(start):
    #시작 노드 처리
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        #현재 노드가 이미 처리된 적 있는 노드면,
        if distance[now] < dist:
            continue
        #아니면,
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
```

# 플로이드 워셜 알고리즘

: 모든 지점에서 다른 모든 지점까지의 최단 경로 모두 구하기

## 특징

- DP의 활용
- 시간 복잡도 : $O(N^3)$ → $N$번의 단계 마다 $O(N^2)$의 연산을 통해 현재 거쳐가는 모든 경로 고려

## 동작 원리

모든 노드에 대해 →$O(N)$
해당 노드를 거쳐가는 경우 고려하기 → $O(^{n-1} P_2)$ == $O(N^2)$

### 상태 정의

> $D_{ab}$  : a에서 b로 가는 최소 비용

이라고 정의했을때, a→b 의 최소 비용은 a에서 b로 바로 가는 비용과 k를 거쳐서, 즉 a→k→b의 비용 중 작은 값이다. 점화식으로 표현하면, 

> $D_{ab} = min(D_{ab}, D_{ak}+D_{kb})$

### Step 0 상태의 초기화

$D_{ab}$  : a에서 b로 가는 최소 비용에 따라 테이블을 초기화한다.
![](https://images.velog.io/images/woo0_hooo/post/5d610451-9997-49aa-bc3a-84550590122f/IMG_AE8F108DBA31-1.jpeg)

출발/도착 | 1번 | 2번 | 3번 | 4번 
----------|-----------|----------|-----------|----------
1번 | 0 | 4 | INF | 6
2번 | 3 | 0 | 7 | INF
3번 | 5 | INF | 0 | 4
4번 | INF | INF | 2 | 0

### Step 1 i번 ~N번 노드를 거쳐가는 경우

- 1번 노드를 거쳐갈때,

     $^{n-1} P_2$가지의 경우의 수가 있다.

    : (2,3), (2,4), (3,2), (3,4), (4,2), (4,3)

    $D_{23} = min(D_{23}, D_{21}+D_{13})$과 같이 나머지 쌍에 대해서도 전부 계산하고, 값을 갱신한다. 

2번~ 4번에 대해서도 마찬가지를로 처리해준다. 

### 최종 결과

출발/도착 | 1번 | 2번 | 3번 | 4번 
----------|-----------|----------|-----------|----------
1번 | 0 | 4 | 8 | 6
2번 | 3 | 0 | 7 | 9
3번 | 5 | 9 | 0 | 4
4번 | 7 | 11 | 2 | 0

## 구현

```python
INF = int(1e9)

n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input()) #시작 노드
graph = [[INF]*(n+1) for _ in range(n+1)] #노드 연결 정보

#자기 자신->자기 자신
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    #각각의 노드를 거쳐가는 경우
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(INF, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
```


# 출처
나동빈님의 이것이 취업을 위한 코딩테스트다 
