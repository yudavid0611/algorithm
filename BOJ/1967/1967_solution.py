import sys
sys.stdin = open('BOJ/1967/1967_input.txt', 'r')
sys.setrecursionlimit(100000)
# input = sys.stdin.readline

class TreeNode:
    def __init__(self, val=0, weight=0):
        self.val = val
        self.ch = []
        self.weight = weight

def postorder(n):
    global max_lengh
    if n:
        w_sum = []
        while n.ch:
            c = n.ch.pop(0)
            w_sum.append(postorder(c))
        w_sum.sort(reverse=True)
        top_2 = sum(w_sum[:2])
        if top_2 > max_lengh:
            max_lengh = top_2
        try:
            return w_sum[0] + n.weight
        except:
            return n.weight


N = int(input())
if N == 1:
    print(0)
else:
    q = []
    root, ch, w = map(int, input().split())
    head = root = TreeNode(root)
    ch = TreeNode(ch, w)
    root.ch.append(ch)
    q.append(ch)

    for _ in range(N-2):
        n, ch, w = map(int, input().split())
        ch = TreeNode(ch, w)
        if n == root.val:
            root.ch.append(ch)
            q.append(ch)
        else:
            while q and root.val != n:
                root = q.pop(0)
            root.ch.append(ch)
            q.append(ch)
    max_lengh = 0
    postorder(head)
    print(max_lengh)