import collections
#collection 모듈
def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]

if __name__=="__main__":
    participant = list(input())
    completion = list(input())
    solution(participant,completion)