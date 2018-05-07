import re
from chap5.pattern_match import sub_list
from chap5.pattern_match import pattern_match_l
from chap5.pattern_match import fail
import random
import jieba


def cut(string): return list(jieba.cut(string))


rule_responses = {
    '?*x hello ?*y': ['How do you do', 'Please state your problem'],
    '?*x I want ?*y': ['what would it mean if you got ?y', 'Why do you want ?y', 'Suppose you got ?y soon'],
    '?*x if ?*y': ['Do you really think its likely that ?y', 'Do you wish that ?y', 'What do you think about ?y', 'Really-- if ?y'],
    '?*x no ?*y': ['why not?', 'You are being a negative', 'Are you saying \'No\' just to be negative?'],
    '?*x I was ?*y': ['Were you really', 'Perhaps I already knew you were ?y', 'Why do you tell me you were ?y now?'],
    '?*x I feel ?*y': ['Do you often feel ?y ?', 'What other feelings do you have?'],
    '?*y 你好 ?*y': ['你好 呀', '请告诉我你的问题'],
    '?*x 我 想 ?*y': ['你觉得 ?y 有什么意义呢？', '为什么你想 ?y', '你可以想想你很快就可以 ?y了'],
    '?*x 我 想要 ?*y': ['你觉得 ?y 有什么意义呢？', '为什么你想 ?y', '你可以想想你很快就可以 ?y了']
}


def get_rule(rule_string_format):
    return {
        # tuple(k.split()): [line.split() for line in v]
        tuple(cut(k)): [cut(line) for line in v]
        for k, v in rule_string_format.items()
    }


def eliza(speech):
    # speech = speech.split()
    speech = cut(speech)

    global rule_responses

    for pattern, responses in get_rule(rule_responses).items():
        match = pattern_match_l(list(pattern), speech)
        if match is not None and match != fail:
            response = random.choice(responses)
            return sub_list(match, response)
    return None


def compose_single_sentene(tree_words):
    results = []
    for e in tree_words:
        if isinstance(e, list):
            results += compose_single_sentene(e)
        else:
            results.append(e)
    return results


if __name__ == '__main__':
    while True:
        sentence = input('USER >>>')
        match = eliza(sentence)
        if match:
            print(' '.join(compose_single_sentene(match)))
        else:
            print('sorry I don\'t know it')



