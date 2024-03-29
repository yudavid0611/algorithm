# 148. Sort List
# 3245 ms / 44.5 MB

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:                                                        # 빈 리스트 노드일 경우 None return
            return

        def merge(left, right):                                             # 합병 과정
            merged_len = len(left) + len(right)
            merged = [0] * merged_len                                       # 두 input을 합친 길이 만큼의 리스트 생성
            merged_top = -1                                                 # 해당 리스트의 마지막 원소 인덱스

            left_front = 0                                                  # left의 첫 번째 원소 인덱스
            right_front = 0                                                 # right의 첫 번째 원소 인덱스
            while left_front < len(left) or right_front < len(right):
                merged_top += 1
                if left_front < len(left) and right_front < len(right):     # left와 right 원소 모두 남아 있는 경우
                    if left[left_front] <= right[right_front]:              # left의 첫 번째 원소가 더 작은 경우 해당 원소 merged에 추가
                        merged[merged_top] = left[left_front]
                        left_front += 1
                    else:                                                   # right의 첫 번째 원소가 더 작은 경우 해당 원소 merged에 추가
                        merged[merged_top] = right[right_front]
                        right_front += 1
                elif left_front < len(left):                                # left의 원소만 남아 있는 경우
                    while left_front < len(left):                           # left의 모든 원소 merged에 추가
                        merged[merged_top] = left[left_front]
                        merged_top += 1
                        left_front += 1
                elif right_front < len(right):                              # right의 원소만 남아 있는 경우
                    while right_front < len(right):                         # right의 모든 원소 merged에 추가
                        merged[merged_top] = right[right_front]
                        merged_top += 1
                        right_front += 1
            return merged

        def merge_sort(arr):
            if len(arr) == 1:                                               # 원소가 1개 남을 때까지 분할
                return arr
            middle = len(arr) // 2                                          # middle 구하기
            left = merge_sort(arr[:middle])
            right = merge_sort(arr[middle:])

            return merge(left, right)
        
        arr = []
        while head:                                                         # ListNode to list
            arr.append(head.val)
            head = head.next
        arr = merge_sort(arr)                                               # 병합정렬
        head = node = ListNode()
        
        arr_top = 0
        while arr_top < len(arr):                                           # list to ListNode
            node.next = ListNode(arr[arr_top])
            node = node.next
            arr_top += 1
            
        return head.next