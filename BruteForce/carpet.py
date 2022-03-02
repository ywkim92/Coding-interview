'''
카펫(https://programmers.co.kr/learn/courses/30/lessons/42842)
'''
import numpy as np
def solution(brown, yellow):
    per = int(np.sqrt(yellow))
    para = per
    while 2*(para+per)+4!=brown:
        while yellow%per!=0:
            per-=1
        para = yellow//per
        print(para, per)
        if 2*(para+per)+4==brown:
            return [para+2, per+2]
        else:
            per-=1
    
    return [para+2, per+2]
