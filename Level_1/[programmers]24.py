# 완주하지 못한 선수
from collections import Counter
def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]