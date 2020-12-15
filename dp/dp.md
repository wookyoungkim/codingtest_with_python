# 중복되는 연산 줄이기
- 연산 속도와 메모리 공간을 최대한으로 활용할 수 있는 효율적인 알고리즘은?

## 수학적 점화식
: 인접한 항 사이의 관계식
**피보나치 수열**의 경우, 
> $a_{n+2} = f(a_{n+1}, a_n) = a_{a+1} + a_n$

로 점화식을 표현할 수 있음
### 점화식의 표현 - 재귀
수학적 점화식을 programming으로 간단하게 표현하려면 재귀함수를 사용하면 된다.
```python
def fibo(x):
    if x == 1 or x ==2:
        return 1
    return fibo(x-1) + fibo(x-2)
```
**<span style="color:Red">-> 문제점</span>**
: f(n)에서 n이 커질수록 수행 시간이 기하급수적으로 늘어남 **O(2^n)**
![](https://images.velog.io/images/woo0_hooo/post/2d7435ea-84ce-47be-8994-4acacb1abcba/IMG_9DA315FA72D5-1.jpeg)
호출 과정을 보면 f(3)만 해도 3번이 호출되는 등 **동일한 함수가 반복적으로 호출**됨을 알 수 있다. 

# Dynamic Programming
## dp란?
큰 문제를 작은 문제로 나누고, 같은 문제를 한번씩만 풀어 효율적으로 문제 해결
> 1. 큰 문제를 작은 문제로 나눌 수 있음
> 2. 작은 문제에서 구한 정답은 큰 문제에서도 동일


을 만족할 때 dp를 사용 가능하다.

## top-down 방법
: 메모제이션 방법 - 한번 구한 결과를 메모리 공간에 메모한 후, 다시 호출시 메모의 결과를 그대로 가져옴
-> 재귀함수를 이용하여 dp 코드 작성
```python
#계산의 결과를 메모제이션하기 위한 리스트
d = [0]*100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    #이미 계산한 적이 있으면
    if d[x] != 0:
        return d[x]
    #이전에 계산하지 않은 경우에는 
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
```

## bottom-up 방법
: smaller instance부터 계산 후 결과를 저장
-> 반복문을 이용하여 dp 코드 작성 (일반적으로 재귀보다 더 효율적)
```python
d = [0]*100

d[1] = 1
d[2] = 2
n = 99

for i inrange(3, n+1):
    d[i] = d[i-1] + d[i-2]
```

-> 이때 **O(N)**의 시간복잡도로 해결 가능

## dp로 문제 해결하기
> 0, 주어진 문제가 dp 유형임을 파악하기
:	완탐으로 접근했을때 너무 오래 걸리면 부분 문제의 중복여부 확인
> 1. recursion 성질이 있는 식 세우기
>	: 일종의 점화식이 됨
>  2. bottom-up으로 smaller instance부터 계산

- list대신 dict 이용 가능
	: 수열처럼 연속적이지 않은 경우
- 단순히 재귀로 작성 후, top-down이 가능하면 dp로 코드 개선해도 됨