---

# 문제풀면서 추가하는 유용한 함수, 모듈들

### 입출력

- 입력받은 문자열을 띄어쓰기로 구분해 정수형으로 저장

    ```python
    list(map(int, input().split())
    ```

- 빠르게 입력받기

    ```python
    import sys
    sys.stdin.readline().rstrip()
    ```

    - rstrip()?

        readline()시 줄바꿈 기호로 입력된 공백문자 제거하기 위해

---

### ord()

: char → int

```python
print(ord('a'))
#97

print(chr(ord('a')))
#a
```

---

### import random

1. `random()`

    : 0.0과 1.0사이 난수

    ```python
    print(random.random())
    ```

2. `randrange(start, stop, step)`

    ```python
    import random

    for i in range(5) :
        print(random.randrange(1, 9, 2))
    ```

3. `randint(start, stop)`

    : 특정 영역 사이의 임의 정수값

4. `choice(list)`

    : 리스트, 튜플, 범위의 숫자 중 하나 반환

    ```python
    import random

    toss = ['가위', '바위', '보']

    for i in range(5) :
        print(random.choice(toss))
    ```

5. shuffle(list)

    : 리스트, 튜플, 문자열 등의 순서 임의로

---

### import datetime

```python
from datetime import datetime

today = datetime.now()

print('년 : %s' % today.year)
print('월 : %s' % today.month)
print('일 : %s' % today.day)
print('시 : %s' % today.hour)
print('분 : %s' % today.minute)
print('초 : %s' % today.second)

print(today.strftime('%Y/%m/%d %H:%M:%S'))
print(today.strftime('%y-%m-%d %p %H:%M'))
```

 - datetime.strftime()
---

### sorted()

- 이터러블로부터 새로 정렬된 리스트
- 각 리스트 정렬할 함수 호출 가능

→ 프로그래머스 가장 큰 수

```python
#대소문자 구분 하지 않기
sorted("This is a test string from Andrew".split(), key=str.lower)

#특정 요소 기준으로 정렬하기
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])
```

- 문자열 길이 순으로 정렬

    ```python
    sorted(Str, key=len)
    ```

---

### enumerate()

- 열거하다 → 리스트, 튜플 등을 인덱스와 함께

    ```python
    a = ['hong','gil','dong']
    b = list(enumerate(randomlist))

    #[(0, 'hong'), (1, 'gil'), (2, 'dong')]
    ```

---

### hash()

- 객체의 해시값을 리턴

    → 응용

    ```python
    #프로그래머스- 완주하지 못한 선수
    def solution(participant, completion):
        answer = ''
        temp = 0
        dic = {}

        for part in participant:
    				#참여 선수 이름의 해쉬값 dictionary에 저장
            dic[hash(part)] = part
    				#참여 선수 해쉬값 전부 합하기
            temp += int(hash(part))
            
                  
        for com in completion:
    				#완주 선수 해쉬값 총합에서 빼기
            temp -= hash(com)
        answer = dic[temp]

        return answer
    ```
    