from bisect import bisect_left, bisect_right

def count_by_range(a, left_val, right_val):
    left_idx = bisect_left(a, left_val)
    right_idx = bisect_right(a, right_val)
    return right_idx - left_idx

#모든 단어를 길이별로 나누어 저장
arr = [[] for _ in range(10001)]
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []

    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1])

    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for query in queries:
        if query[0] != "?":
            #?가 끝에
            res = count_by_range(arr[len(query)], query.replace("?", "a"), query.replace("?", "z"))
        else:
            res = count_by_range(reversed_arr[len(query)], query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
        answer.append(res)
    return answer