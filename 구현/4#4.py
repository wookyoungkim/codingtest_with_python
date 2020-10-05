def rotate_a_matrix_by_90_degrees(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

#자물쇠의 중간부분이 모두 1인지?
def check(new_lock):
    lock_length = len((new_lock)) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(key)
    m = len(lock)
    new_lock = [[0]*(m*3) for _ in range(m*3)]

    if all(0 not in l for l in lock):
        return True

    for i in range(m):
        for j in range(m):
            new_lock[i+m][j+m] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degrees(key)
        for x in range(m*2):
            for y in range(m*2):
                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(n):
                    for j in range(n):
                        new_lock[x+i][y+j] -= key[i][j]
    return False