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
from utilities import lmap
from collections import defaultdict


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
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article => 这个 | 一个
noun => 男人 | 篮球 | 女人 | 桌子
verb => 打 | 拿 | 看见 | 喜欢
Adj => 黑色的 | 蓝色的 | 漂亮的 | 坚固的
"""

more_complicated_grammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article Adj* noun PP*
Adj* => null | Adj Adj*
PP* => null | PP PP*
PP => prep noun_phrase
Adj => big | little | blue | green
prep => to | in | by | with
verb_phrase => verb noun_phrase
verb => hit | took | saw | liked
noun => man | ball | woman | table
Article => the | a
"""

complicated_grammar = """
sentence => noun-phrase verb-phrase
noun-phrase => Article Adj* Noun PP* | Name | Pron
verb-phrase => Verb noun-phrase PP*
PP* => null | PP PP*
Adj* => null | Adj Adj*
PP => Prep noun-phrase
Prep => to | in | by | with | on
Adj => big | little | blue | green | adiabatic
Article => the | a 
Name => Pat | Kim | Lee | Terry | Robin
Noun => man | ball | woman | table
Verb => hit | took | saw | liked
Pron => he | she | it | these | those | that
"""

grammer = convert_grammar(simple_grammar)


def rewrites(category):
    return grammer.get(category, None)


def generate(phrase):
    if isinstance(phrase, list):
        return mappend(generate, phrase)
    elif phrase not in grammer:
        return [phrase]
    else:
        return generate(random.choices(rewrites(phrase)))


def generate_tree(phrase):
    if isinstance(phrase, list):
        return mappend(generate_tree, phrase)
    elif phrase not in grammer:
        return [phrase]
    else:
        return [phrase] + generate_tree(random.choices(rewrites(phrase)))


def format_result(listed_result):
    return ' '.join(filter(lambda x: x != 'null', listed_result))


def format_tree_result(tree_result):
    if not isinstance(tree_result, list): return tree_result
    else:
        root = tree_result[0]
        tree_syntax = defaultdict(list)
        for sub_tree in tree_result[1:]:
            tree_syntax[root].append(format_tree_result(sub_tree))
        return dict(tree_syntax)


if __name__ == '__main__':
    print((format_result(generate(['sentence']))))
