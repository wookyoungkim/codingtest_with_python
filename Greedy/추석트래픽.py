def checktraffic(time, logs):
    count = 0
    start=time
    end=time+1
    for log in logs:
        if log[1] >= start and log[0] < end:
            count += 1
    return count

def solution(lines):
    answer = 0
    ans = 0
    logs = []
    
    for line in lines:
        date, time, sec = line.split()
        h, m, s = time.split(":")
        end = int(h)*60*60 + int(m)*60 + float(s)
        start = end - float(sec[:-1]) + 0.001
        logs.append([start, end])
    
    logs.sort()
    print(logs)
    time = logs[0][0]
    for log in logs:
        answer=max(answer,checktraffic(log[0],logs),checktraffic(log[1],logs))
        
    return answer

print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))