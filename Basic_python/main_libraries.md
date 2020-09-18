      

# 주요 라이브러리


## 내장함수

```python
#리스트의 원소 합
result = sum([1,2,3,4,5])

#리스트의 최소값
result = min([1,2,3,4,5])

#리스트의 최대값
result = max([1,2,3,4,5])

#문자열 수식 계산
result = eval("(3+5)*7")

```

---

## itertools

- permutations

    : r개의 데이터를 뽑아서 일렬로 나열하는 모든 경우

- combinations

    : r개의 데이터를 뽑아서 순서 상관없이 나열하는 모든 경우

- product

    : r개의 데이터를 뽑아서 일렬로 나열하는데 중복 허용

- combinations_with_replacement

    : r개의 데이터를 뽑아서 순서 상관없이 나열하는데 중복 허용 

```python
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

perm = list(permutations(data, 3))
[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

comb = list(combinations(data, 3))
[('A', 'B', 'C')]

prod = list(product(data, repeat = 2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

comb_w = list(combinations_with_replacement(data, 2))
[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

```

---

## bisect

- **정렬된 배열**에서 특정 원소 찾을때

    → O(logN)에 동작

- `bisect_left(a, x)`

    : 정렬된 순서를 유지하면서 리스트 a에 데이터 x 삽입할 가장 왼쪽 인덱스 찾기

- `bisect_right(a, x)`

    : 정렬된 순서를 유지하면서 리스트 a에 데이터 x 삽입할 가장 오른쪽 인덱스 찾기

    → 값이 특정 범위에 속하는 원소의 개수

```python
from bisect import bisect_right, bisect_left

a = [1,2,3,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))
```

- `count_by_range(a, left_value, right_value)`

    : 정렬된 리스트 a 에서 **left_value≤x≤ right_value**인 x개수를 **O(logN)**으로

    ```python
    from bisect import bisect_right, bisect_left

    def count_by_range(a, left_value, right_value):
        rindex = bisect_right(a, right_value)
        lindex = bisect_left(a, left_value)
        return rindex-lindex

    a = [1,2,3,4,4,8]
    x = 4

    print(count_by_range(a,4,4))
    ```

---

## collections

- deque

    : 연속적으로 나열된 데이터의 시작/끝에 데이터 삽입/삭제시 **O(1)**

    ↔ list는 삽입, 삭제, 인덱싱, 슬라이싱 등 가능하지만 삭제시 **O(N)**

    - 삽입 :  append(), appendleft()

    - 삭제 :  pop(), popleft()

    **→ deque를 queue로 사용 ?**

    : 삽입은 append(), 삭제는 popleft()

- Counter

    : 등장 횟수를 세는 기능 → iterable 객체 내에 원소가 몇번 등장했는지

    ```python
    from collections import Counter

    counter = Counter(['red', 'blue', 'red', 'green', 'blue'])

    print(counter['red'])
    print(counter['blue'])
    print(counter['green'])

    print(dict(counter))
    #{'red': 2, 'blue': 2, 'green': 1}
    ```

---

## math

- `factorial(x)`
- `sqrt(x)`
- `gcd(a, b)`