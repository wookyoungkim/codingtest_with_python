def solution(phone_book):
    
    sorted_phone = sorted(phone_book, key=len)
    
    for i in range(len(sorted_phone)):
        for j in range(i+1, len(sorted_phone)):
            if sorted_phone[j].startswith(sorted_phone[i]):
                return False
    return True