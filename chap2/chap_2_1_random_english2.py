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
from utilities import mappend
from utilities import assoc
from utilities import lmap


def convert_grammar(grammar):
    dict_grammar = {}
    for line in grammar.split('\n'):
        if not line: continue
        left, right = line.split('=>')
        right = lmap(lambda rule: rule.split(), right.split('|'))
        dict_grammar[left.strip()] = right

    return dict_grammar


simple_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article noun
verb_phrase => verb noun_phrase
Article => the | a
noun => man | ball | woman | table
verb => hit | took | saw | liked
"""

grammer = convert_grammar(simple_grammar)
print(grammer)


def rewrites(category):
    return grammer.get(category, None)


def generate(phrase):
    if isinstance(phrase, list):
        return mappend(generate, phrase)
    elif rewrites(phrase):
        return generate(random.choices(rewrites(phrase)))
    else:
        return [phrase]


if __name__ == '__main__':
    print(generate(['sentence']))
