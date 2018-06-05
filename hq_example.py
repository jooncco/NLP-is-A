import numpy as np
import heapq as hq

def top_n(iterable, n):
    '''
    Returns top n items in descending order.
    '''
    h = []
    for item in iterable:
        hq.heappush(h, item)
    arr_sorted = [hq.heappop(h) for i in range(0, len(h))]
    return [arr_sorted[-i] for i in range(1, n+1)]

brain = dict()
brain['dummy'] = [ ('concept1', 0.8), ('concept2', 0.2) ]
print(brain.__contains__('dummy_'))