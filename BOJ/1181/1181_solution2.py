import sys
sys.stdin = open('BOJ/1181/1181_input.txt', 'r')

words_num = int(input())

word_list = [[] for _ in range(51)]                 # 단어 길이별로 단어들을 저장할 2차원 리스트

for _ in range(words_num):                          # 단어 받아서 2차원 리스트에 넣기
    w = input()
    word_list[len(w)].append(w)
        
for i in word_list:                                 # 2차원 리스트 순회
    if i != None:                                   # 단어들이 존재하는 원소 리스트일 경우
        i = list(set(i))                            # 중복 제거
        i.sort()                                    # 사전순 정렬
        for j in i:
            print(j)                                # 출력