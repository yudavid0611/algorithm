# 이진탐색
## 설명
1. 배열을 정렬한다.
2. 배열의 중앙값과 target을 비교한다.
3. 값 비교
  - target > 중앙값 -> 중앙값 기준 오른쪽 배열의 중앙값과 다시 비교
  - target < 중앙값 -> 중앙값 기준 왼쪽 배열의 중앙값과 다시 비교
4. 종료
  - 일치하는 값을 찾았을 때
  - 더 이상 비교할 수 있는 배열이 없을 때

## 풀이
1. 반복문
  ``` python
  def binary_search(target, searched_list):
    while True:
      low = 0
      high = len(searched_list)
      mid = int((high-low)/2)

      if target == searched_list[mid]:
        return True
      elif target > searched_list[mid]:
        low = mid + 1
      else:
        high = mid - 1
    return False
  ```
2. 재귀함수

