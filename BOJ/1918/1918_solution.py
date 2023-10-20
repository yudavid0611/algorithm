import sys
from collections import deque
sys.stdin = open('1918_input.txt')
input = sys.stdin.readline

operation = deque(list(input().rstrip()))

# 우선순위가 높은 순서대로 가중치 부여
weight = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
    }

answer = []

# 연산자를 처리할 스택
operator = []

while operation:
    now = operation.popleft()

    # 알파벳일 경우 answer에 바로 추가
    if now.isalpha():
        answer.append(now)
    
    # 연산자일 경우
    else:
        # operator가 비었거나 now가 여는 괄호일 경우
        if not operator or now == '(':
            operator.append(now)
        
        else:
            # 스택에서 연산자 pop
            op = operator.pop()

            # now가 닫는 결호일 경우
            if now == ')':
                # 큐
                q = deque()
                
                # 여는 괄호가 나오기 전까지의 모든 연산자 큐에 추가
                while True:
                    if op == '(':
                        break
                    q.append(op)
                    op = operator.pop()
                
                # 큐에서 answer로 옮기기
                while q:
                    op = q.popleft()
                    answer.append(op)

            # now가 일반 연산자이고, op가 여는 괄호일 경우 그대로 스택에 넣기
            elif op == '(':
                operator.append(op)
                operator.append(now)
            
            # op와 now가 모두 일반 연산자일 경우
            else:                
                # now의 weight이 op의 weight보다 클 경우
                if weight[now] > weight[op]:
                    operator.append(op)
                    operator.append(now)
                
                # op의 weight이 더 크거나 같을 경우
                else:
                    answer.append(op)
                    # 여는 괄호가 나오기 전 또는 weight이 now보다 더 작은 연산자가 나올 때까지 answer에 추가
                    while operator:
                        op = operator.pop()
                        if op == '(' or weight[now] > weight[op]:
                            operator.append(op)
                            break
                        answer.append(op)

                    operator.append(now)

# 남은 연산자 answer로 옮기기 
while operator:
    answer.append(operator.pop())

print(''.join(answer))