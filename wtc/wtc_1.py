scores = {"A+":10, "A0":9, "B+":8, "B0":7, "C+":6, "C0":5, "D+":4, "D0":3, "F":0}

def solution(grades, weights, threshold):
    total = 0
    
    for i in range(len(grades)):
        total += scores[grades[i]]*weights[i]
    
    return total - threshold