"""
But when we meet the more complicated grammer such as :

NP => Article + Adj* + Noun + PP*
Adj* => null, Adj + Adj*
PP* => null, PP + PP*
PP => Prep + NP
Adj => big, little, blue, green
Prep => to, in, by, win

the simple function will not work for this.
"""
import random
from functools import reduce


def mappend(func, elements):
    return reduce(lambda a, b: a + b, map(func, elements))


def assoc(key, lists):
    for l in lists:
        if len(lists) >= 1 and l[0] == key: return l
    else:
        return None


simple_grammar = [
    ['sentence', '->', ['noun_phrase', 'verb_phrase']],
    ['noun_phrase', '->', ['Article', 'noun']],
    ['verb_phrase', '->', ['verb', 'noun_phrase']],
    ['Article', '->', 'the', 'a'],
    ['noun', '->', 'man', 'ball', 'woman', 'table'],
    ['verb', '->', 'hit', 'took', 'saw', 'liked']
]

grammer = simple_grammar


def rule_lhs(rule): return rule[0]


def rule_rhs(rule): return rule[2:]


def rewrites(category):
    rewrite_elements = assoc(category, grammer)
    if rewrite_elements: return rule_rhs(rewrite_elements)
    else: return None


def generate(phrase):
    if isinstance(phrase, list):
        return mappend(generate, phrase)
    elif rewrites(phrase):
        return generate(random.choices(rewrites(phrase)))
    else:
        return [phrase]


if __name__ == '__main__':
    print(generate(['sentence']))
