from collections import deque
import sys


def count(paperF, weights):
    N = int(paperF[0])
    paper = int(paperF[1])
    max_index = weights.index(max(weights))
    l = len(weights)
    # if max(weights) == min(weights) and l >= 2:
    #     return paper
    if max_index == paper:
        return 1
    else:
        paperF[0] = N - 1
        if max_index > paper:
            for i in range(max_index + 1):
                weights.append(weights.popleft())
            paper = l - max_index - 1 + paper
            paperF[1] = paper
            weights.pop()
            return 1 + count(paperF, weights)
        else:
            for i in range(max_index + 1):
                weights.append(weights.popleft())
            paper = paper - max_index - 1
            paperF[1] = paper
            weights.pop()
            return 1 + count(paperF, weights)


Test_case = int(input())
for i in range(Test_case):
    paperF = sys.stdin.readline().split()
    weights = deque(sys.stdin.readline().split())
    print(count(paperF, weights))
