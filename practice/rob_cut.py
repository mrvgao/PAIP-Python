from functools import lru_cache

length = [0, 1, 2, 4, 5, 10]
prices = [0, 1, 3, 5, 8, 20]

length_price = {l: p for l, p in zip(length, prices)}


@lru_cache(maxsize=1024)
def cut_rob(seg):
    if seg == 1 or seg == 0:
        return length_price[seg]
    else:
        return max(length_price[i] + cut_rob(seg - i)
                   for i in range(1, seg) if i in length_price)


options = {}


def cut_rob_with_mark(seg):
    if seg == 1 or seg == 0:
        return length_price[seg]
    else:
        candidates = ((length_price[i] + cut_rob_with_mark(seg - i), i)
                      for i in range(1, seg + 1) if i in length_price
                      )
        optimal = max(candidates, key=lambda x: x[0])
        options[seg] = (optimal[1], seg - optimal[1])
        return optimal[0]


def restore_solution(seg):
    global options
    r, b = options.get(seg, (seg, 0))
    if r == 0 or b == 0:
        return r, b
    else:
        return restore_solution(r) + restore_solution(b)


print(cut_rob(8))
print(cut_rob(9))
print(cut_rob_with_mark(9))
print(restore_solution(8))
print(restore_solution(9))
