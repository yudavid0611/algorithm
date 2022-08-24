import sys
sys.stdin = open('BOJ/1181/1181_input.txt', 'r')

words_num = int(input())

result = [0]
for _ in range(words_num):
    w = input()

    for idx in range(len(result)):
        if result[idx] != 0:
            if len(w) < len(result[idx]):           # 기존 단어보다 길이가 짧을 경우
                result.insert(idx, w)
                break
            elif len(w) == len(result[idx]):
                if w != result[idx]:
                    if w < result[idx]:
                        result.insert(idx, w)
                    else:
                        result.insert(idx+1, w)
                break
        else:
            result.insert(idx, w)

for i in result[:-1]:
    print(i)