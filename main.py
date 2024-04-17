import math,queue
from collections import Counter

####### Problem 3 #######

test_cases = [
    ('book', 'back'),
    ('kookaburra', 'kookybird'),
    ('elephant', 'relevant'),
    ('AAAGAATTCA', 'AAATCA')
]
alignments = [
    ('b--ook', 'bac--k'),
    ('kook-ab-ur-ra', 'kooky-bi-rd--'),
    ('-ele-phant', 'relev--ant'),
    ('AAAGAATTCA', 'AAA---T-CA')
]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if not S:
        return len(T)
    if not T:
        return len(S)

    if S[0] == T[0]:
        return MED(S[1:], T[1:])
    else:
        return 1 + min(MED(S, T[1:]),  
                       MED(S[1:], T)) 

def fast_MED(S, T, MED={}):

    if (S, T) in MED:
        return MED[(S, T)]

    if not S:
        MED[(S, T)] = len(T)
    elif not T:
        MED[(S, T)] = len(S)
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    else:
        MED[(S, T)] = 1 + min(fast_MED(S, T[1:], MED),
                                         fast_MED(S[1:], T, MED))
    return MED[(S, T)]

def fast_align_MED(S, T, MED={}):

    if (S, T) in MED:
        return MED[(S, T)]

    if not S:
        MED[(S, T)] = ("-" * len(T), T)
    elif not T:
        MED[(S, T)] = (S, "-" * len(S))
    elif S[0] == T[0]:
        aligned_s, aligned_t = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (S[0] + aligned_s, T[0] + aligned_t)
    else:
        insert_s, insert_t = fast_align_MED(S, T[1:], MED)
        delete_s, delete_t = fast_align_MED(S[1:], T, MED)
        if 1 + len(insert_s) <= 1 + len(delete_s):
            MED[(S, T)] = ("-" + insert_s, T[0] + insert_t)
        else:
            MED[(S, T)] = (S[0] + delete_s, "-" + delete_t)
    return MED[(S, T)]
