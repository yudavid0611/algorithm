import sys
import bisect
from collections import deque
sys.stdin = open('1715_input.txt')

N = int(input())

cards = [int(input()) for _ in range(N)]

cards.sort()

cards = deque(cards)

answer = 0
while len(cards) > 1:
    card1 = cards.popleft()
    card2 = cards.popleft()
    combined = card1 + card2
    answer += combined
    combineda_idx = bisect.bisect_left(cards, combined)
    cards.insert(combineda_idx, combined)

print(answer)