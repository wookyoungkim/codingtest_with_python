def get_formal_time(time):
    m, s = divmod(time, 60)
    h, m = divmod(m, 60)
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)
    
def get_time(time):
    H, M, S = map(int, time.replace(":", " ").split())
    return H*60*60 + M*60 + S

def solution(play_time, adv_time, logs):
    answer = 0
    log_list = []
    total_duration = get_time(play_time)
    adv_duration = get_time(adv_time)
    
    # 1. 로그 파싱
    for log in logs:
        start, end = log.split("-")
        start_time = get_time(start)
        end_time = get_time(end)
        log_list.append([start_time, end_time])
    
    # 2. 매 초별 누적 시청자수 계산하기
    total_time = [0]*(total_duration+1)
    for log in log_list:
        for i in range(log[0], log[1]+1):
            total_time[i] += 1

    max_val = 0
    # 3. 0초 ~ 전체 재생시간 - 광고 재생 시간까지 최고 시청자수 구하기
    for i in range(total_duration-adv_duration+1) :
        count = 0
        for j in range(i, i+adv_duration+1):
            count += total_time[j]
        if max_val < count:
            max_val = count
            answer = i
    #다시 시간 형식으로
    return get_formal_time(answer-adv_duration)

print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))