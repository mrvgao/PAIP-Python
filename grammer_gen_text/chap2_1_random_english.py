"""
Generate random English sentences.

Grammar:
    Sentence => Noun-Phrase + Verb-Phrase
    Noun-Phrase => Article + Noun
    Verb-Phrase => Verb + Noun-Phrase
    Article => the, a, ...
    Noun => man, ball, woman, table. . .
    Verb => hit, took, saw, liked. . .
"""
# straight forward solution

import random
from utilities import one_of

def sentence(): return noun_phrase() + verb_phrase()
def noun_phrase(): return article() + noun()
def verb_phrase(): return verb() + noun_phrase()
def article(): return one_of(['the', 'a'])
def noun(): return one_of(['man', 'ball', 'wowan', 'table'])
def verb(): return one_of(['hit', 'took', 'saw', 'liked'])


