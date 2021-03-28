def solution(dirs):
    directions = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    road = set()
    cur_x, cur_y = (0,0)
    
    for d in dirs:
        next_x, next_y = cur_x + directions[d][0], cur_y + directions[d][1]
        if -5<= next_x <=5 and -5<= next_y <=5:
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2