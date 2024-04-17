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

def MED(source, target):
    # TO DO - modify to account for insertions, deletions and substitutions
    if not source:
        return len(target)
    if not target:
        return len(source)

    if source[0] == target[0]:
        return MED(source[1:], target[1:])
    else:
        return 1 + min(MED(source, target[1:]),  
                       MED(source[1:], target)) 

def fast_MED(source, target, memo=None):
    # TODO -  implement top-down memoization
    if memo is None:
        memo = {}

    if (source, target) in memo:
        return memo[(source, target)]

    if not source:
        memo[(source, target)] = len(target)
    elif not target:
        memo[(source, target)] = len(source)
    elif source[0] == target[0]:
        memo[(source, target)] = fast_MED(source[1:], target[1:], memo)
    else:
        memo[(source, target)] = 1 + min(fast_MED(source, target[1:], memo),
                                         fast_MED(source[1:], target, memo))
    return memo[(source, target)]

def fast_align_MED(source, target, memo=None):
    # TODO - keep track of alignment
    if memo is None:
        memo = {}

    if (source, target) in memo:
        return memo[(source, target)]

    if not source:
        memo[(source, target)] = ("-" * len(target), target)
    elif not target:
        memo[(source, target)] = (source, "-" * len(source))
    elif source[0] == target[0]:
        aligned_s, aligned_t = fast_align_MED(source[1:], target[1:], memo)
        memo[(source, target)] = (source[0] + aligned_s, target[0] + aligned_t)
    else:
        insert_s, insert_t = fast_align_MED(source, target[1:], memo)
        delete_s, delete_t = fast_align_MED(source[1:], target, memo)
        if 1 + len(insert_s) <= 1 + len(delete_s):
            memo[(source, target)] = ("-" + insert_s, target[0] + insert_t)
        else:
            memo[(source, target)] = (source[0] + delete_s, "-" + delete_t)
    return memo[(source, target)]