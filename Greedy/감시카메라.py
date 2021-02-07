def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[1])  # 진출 지점 기준으로 정렬
    camera = -30001 #카메라의 초기 위치
    
    for route in routes:
        if camera < route[0]: #카메라의 위치가 더 작으면 -> 카메라 못만남
            answer += 1
            camera = route[1]
    
    return answer