from collections import deque
from copy import deepcopy

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    
    total = q1_sum + q2_sum
    
    target, remainder = divmod(total, 2)
    
    limit = len(queue1) * 3
    
    # 나머지가 있을 경우 원소 합을 같게 만들 수 없음
    if remainder:
        return -1
    
    task = 0
    while q1_sum != target:
        if q1_sum > target:
            popped = queue1.popleft()
            queue2.append(popped)
            q1_sum -= popped
            
        elif q1_sum < target:
            popped = queue2.popleft()
            queue1.append(popped)
            q1_sum += popped
        
        task += 1
        
        if task > limit:
            return -1
        
    return task
