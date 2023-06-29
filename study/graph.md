# Graph

<br>

> reference: 『파이썬 알고리즘 인터뷰』, 「12장: 그래프

<br>

## 기본 개념
- 그래프란?: 객체의 일부 쌍(pair)들이 연관되어 있는 객체 집합 구조
- 해밀턴 경로: 각 정점을 한 번씩 방문하는 무향, 유향 그래프 경로
        - 해밀턴 순환: 모든 정점을 한 번씩 방문하고 원래의 출발점으로 돌아오는 경로
        - 외판원 문제(Traveling Salesman Problem): 최단 거리 해밀턴 순환을 찾는 문제
- 그래프 순회(자세한 내용은 'graph_search' 폴더 참고)
        - DFS(깊이 우선 탐색)
        - BFS(너비 우선 탐색)
- 백트래킹: 해결책에 대한 후보를 구축해나감과 동시에 해결책이 될 수 없는 후보들이 생길 경우 즉시 해당 후보들을 포기하며 답을 찾는 알고리즘. 제약 충족 문제(constraint satisfacion problems)에 유용
        - 제약 충족 문제: 제약 조건을 충족하는 상태(states)를 찾아내는 문제. 스도쿠, 4색 문제 등이 그 예이다.

<br>

## 그래프 표현법
- 인접 행렬(adjacency matrix): 연결되어 있는 정점들은 1로, 연결되어 있지 않은 경우 0으로 표시한 행렬
- 인접 리스트(adjacency list): 딕셔너리로 표현. 출발노드를 key로, 도착노드(들)를(을) value(리스트)로 넣는다.


<br>

## 관련 문제
- LeetCode 200: [Number of Islands](https://github.com/yudavid0611/algorithm/blob/master/LeetCode/200.py)
- LeetCode 17: [Letter Combinations of a Phone Number](https://github.com/yudavid0611/algorithm/blob/master/LeetCode/17.py)
- LeetCode 77: [Combinations](https://github.com/yudavid0611/algorithm/blob/master/LeetCode/77.py)
- LeetCode 78: [Subsets](https://github.com/yudavid0611/algorithm/blob/master/LeetCode/78.py)
- LeetCode 39: [Combination Sum](https://github.com/yudavid0611/algorithm/blob/master/LeetCode/39.py)