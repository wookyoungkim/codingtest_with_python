# 코딩테스트를 위한 파이썬 문법


## 기본 문법

---

### 전역변수

```python
a=0

def func():
	global a
	a+=1
```

### 자료형

- 실수형

    - 지수 표현방식 제공 

    → 최단경로 문제에서 가능한 최대값이 10억미만일때 자주 사용 

    ```python
    a = 1e9
    #10^9표현 

    ```

---

### **산술연산자**

- 나누기

    ```python
    #나머지 구하기
    x = 10 % 3
    #몫 구하기
    y = 10 // 3
    #나누기 -> 실수로 반환 
    z = 7 / 3 
    ```

- 거듭제곱

    ```python
    x = 2**3
    ```

---

### **문자열**

- 문자열 반복

    ```python
    hi = '안녕'*5
    ```

- 문자열 포매팅

    % 이용

    ```python
    height = 172.5
    a = '키는 %.2f입니다.' % height

    print(a)
    ```

    str.format 이용

    → 자료형 몰라도 가능

    ```python
    test = 'Hello {}'.format('Bob')

    print(test)
    ```

    자릿수 맞추기

    ```python
    year = 2020
    month = 3
    day = 5

    a = '%d-%02d-%02d' % (year, month, day)
    print(a)
    ```

    역순 출력

    ```python
    #방법 1
    	def strReverse1(string):
        return string[::-1]
    		#튜플, 리스트 전부 적용 가능

    #방법 2
    		def strReverse(string):
        return reversed(string)
        
    in_string = input('문자열을 입력하세요: ')
    result = strReverse(in_string)
    print(''.join(result))
    ```

    비교

    ```python
    #완전일치
    if str1 == str2:

    #부분일치
    if str1 in str2:

    #전방일치
    if str1.startswith(str2):

    #후방일치
    if str1.endswith(str2):
    ```

---

### 화면출력

- separator

    : 각 항목사이의 문자 정의

    ```python
    year = 2020
    month = 3
    day = 5

    print(year, month, day, sep='/')
    ```

- end

    : 출력 내용의 마지막에 들어갈 문자열

    ```python
    a = '안녕하세용'
    print(a, end='')
    ```

---

### 입력

- input()

    ```python
    name = input('이름을 입력하세요: ')

    print('%s님 반갑습니다.' % name)
    ```

---

### 조건문

- 조건부 표현식

    ```python
    score = 85
    result = "Success" if score>=80 else "Fail"
    ```

    ```python
    a = [1,2,3,4,5,5,5]
    remove_set = {3,5}

    result = [i for i in a if i not in remove_set]
    ```

---

### 반복문

1. `range(종료값)`

    > 0 ~ 종료값-1의 정수 범위(1씩 증가)의 값을 가집니다.

2. `range(시작값, 종료값)`

    > 시작값에서 종료값-1의 정수 범위(1씩 증가)의 값을 가집니다.

3. `range(시작값, 종료값, 증가값)`

    > 시작값 ~ 종료값~1의 정수 범위를 갖는데, 각 정수 사이의 간격은 증가값에 의해 결정됩니다.

4. `range(시작값, 종료값, 감소값)`

    > 감소값, 즉 음수의 값을 가지는 경우 범위는 시작값 ~ 종료값+1 이 됩니다.

---

### 리스트

- **`index(a)`**

    : 리스트 요소 a의 인덱스 값 return

    ```python
    #뒤에서 첫번째
    print(a[-1])

    #뒤에서 세번째 
    print(a[-3])
    ```

- **`pop(x)`**

    : x번째 인덱스의 요소를 리스트에서 삭제

- `insert(x,y)`

    : x번째에 y추가

- **`remove(a)`**

    :  리스트에서 값 a를 가진 요소 삭제

    → 여러개면 하나만

- `count(a)`

    : 리스트에서 값 a를 가지는 원소 개수 

    ```python
    a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    x = a.index(30)
    print(x)

    a.pop(x)     # del a[x]와 동일
    print(a)

    a.remove(90)
    print(a)

    a.clear()
    print(a)
    ```

- `sort()`

    : 리스트의 오름차순 정렬

    → 내림차순은 reverse=True 이용 

    ```python
    list2 = [-7, 1, 5, 8, 3, 9, 11, 13]
    list2.sort()
    print(list2)

    list2.sort(reverse=True)
    print(list2)
    ```

- List comprehension

    ```python
    array = [i for i in range(20) if i%2 == 1]

    #array=[]
    #for i in range(20):
        #if i%2 == 1:
            #array.append(i)
    ```

→ 리스트 컴프리헨션 이용해 2차원 리스트초기화

    ```python
    n=3
    m=4
    array = [[0]*m for _ in range(n)]
    ```

- _는 ?

    반복을 수행하되 반복을 위한 변수값을 무시할때

---

### 튜플

- 튜플과 리스트

    : 튜플은 소괄호() 사용, 요소의 수정/삭제 불가능

    → 리스트에 비해 공간효율적, 각 원소의 성질이 다를떄 주로 사용

- 삭제

    ```python
    #tuple1의 존재 자체를 완전히 삭제
    del tuple1
    ```

---

### 딕셔너리

- key와 value로 구성

    ```python
    members = {'name':'김우경', 'age':25, 'phone':'010-3787-3146'}

    #접근
    print(members['name'])
    ```

- 추가, 수정, 삭제 가능
- 관련 함수

    ```python
    key_list = data.keys()

    value_list = data.values()
    ```

- for문 활용

    ```python
    phones = {'갤럭시 노트8': 2017,  '갤럭시 S9': 2018, '갤럭시 노트10': 2019, '갤럭시 S20': 2020}
    print(phones)

    for phone in phones :
        print('%s => %s' % (phone, phones[phone]))

    print(len(phones))
    ```

- 정렬

    ```python
    fruits = { 'apple': 2, 'banana' : 1, 'pear' : 2, 'melon' : 0, 'plum' : 1}

    #key 기준 정렬
    res = sorted(fruits)
    print(res)

    #value 기준 정렬
    res = sorted(fruits, key=lambda k : fruits[k])
    print(res)
    ```

---

### 집합

- 특징

    : 중복 허용x, 순서 x

- 초기화

    ```python
    data = set([1,2,3,4,5])

    data = {1,2,3,4,5}
    ```

- 연산

    : 합집합, 교집합, 차집합 제공

    ```python
    a = set([1,2,3,4,5])
    b = set([3,4,5,6,7])

    print(a|b)
    print(a&b)
    print(a-b)
    ```

- 관련 함수

    ```python
    data = set([1,2,3])

    data.add(4)
    #원소 여러개 추가
    data.update([5,6])
    #특정값 갖는 원소 삭제
    data.remove(3)
    ```

---

### 함수

- n개의 매개변수

    : 매개변수의 개수 정하지 x

    ```python
    def average(*scores) :
        sum = 0
        for i in range(len(scores)) :
            sum += scores[i]
        
        avg = sum/len(scores)
        print('%d과목의 평균 : %.2f' % (len(scores), avg))

    average(80, 90, 100)
    average(75, 80, 94, 78)
    average(80, 73, 76, 86,82)
    ```

- 할당에 의한 호출(Call by Assignment)

    : 함수 호출 시 전달되는 값이나 변수의 데이터 형에 따라 자동으로 call by value나 call by reference 선택

    ```python
    #call by value
    def func(x) :
        x = 100
        print('func() : x = ', x, ', id =', id(x))

    x = 10
    print('메인 : x = ', x, ', id =',id(x))
    func(x)
    print('메인 : x = ', x, ', id =', id(x))
    ```

    - id()

    ```python
    # call by reference
    def func(x) :
        x[0] = 100
        print('func() : x = ', x, ', id =', id(x))

    x = [1,2,3]
    print('메인 : x = ', x, ', id =', id(x))
    func(x)
    print('메인 : x = ', x, ', id =', id(x))
    ```

- 람다 함수

    : `**lambda 매개변수 1, 매개변수2, ... : 수식**`

    ```python
    f = lambda x, y, z: x+y+z
    print(f(10, 20, 30))

    def mul(n) :
        return lambda x : x * n

    g = mul(3)
    h = mul(5)

    print(g(10))
    print(h(10))
    ```

- 전역변수

    : global 이용해 선언

- 파일 쓰기

    ```python
    #파일객체 = open(파일명, 파일모드, 인코딩)
    file = open('sample.txt', 'w', encoding='utf8')
    ```

    - 파일모드

---

### 파이썬의 객체지향

    ```python
    class  Member:
        def __init__(self, name, age) :
            self.name = name
            self.age = age

        def showMember(self) :
            print('이름 : %s' % self.name)
            print('나이 : %d' % self.age)
            
    mem1 = Member('홍지수', 24)
    mem1.showMember()
    mem2 = Member('안지영', 20)
    mem2.showMember()
    ```

- 상속

    ```python
    class Animal:
        def __init__(self, name):
            self.name = name

        def printName(self):
            print(self.name)
            
    class Dog(Animal):
        def __init__(self, name, sound):
            super().__init__(name)
            self.sound = sound
            
        def printSound(self):
            print(self.sound)

    dog1 = Dog('행복이','멍멍~~~')
    dog1.printName()
    dog1.printSound()
    ```

---

# 유용한 함수, 모듈들

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