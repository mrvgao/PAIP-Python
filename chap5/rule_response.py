import re
from chap5.pattern_match import sub_list
from chap5.pattern_match import pattern_match_l
from chap5.pattern_match import fail
from chap5.pattern_match import is_variable
from chap5.pattern_match import is_segment_pattern
import random
import jieba


rule_responses = {
    '?*x hello ?*y': ['How do you do', 'Please state your problem'],
    '?*x I want ?*y': ['what would it mean if you got ?y', 'Why do you want ?y', 'Suppose you got ?y soon'],
    '?*x if ?*y': ['Do you really think its likely that ?y', 'Do you wish that ?y', 'What do you think about ?y', 'Really-- if ?y'],
    '?*x no ?*y': ['why not?', 'You are being a negative', 'Are you saying \'No\' just to be negative?'],
    '?*x I was ?*y': ['Were you really', 'Perhaps I already knew you were ?y', 'Why do you tell me you were ?y now?'],
    '?*x I feel ?*y': ['Do you often feel ?y ?', 'What other feelings do you have?'],
    '?*y你好?*y': ['你好呀', '请告诉我你的问题'],
    '?*x我想?*y': ['你觉得?y有什么意义呢？', '为什么你想?y', '你可以想想你很快就可以?y了'],
    '?*x我想要?*y': ['?x想问你，你觉得?y有什么意义呢?', '为什么你想?y', '?x觉得，你可以想想你很快就可以有?y了', '你看?x像?y不', '我看你就像?y'],
}


concat = ''.join


def merge_variable(split_tokens):
    results = []
    i = 0
    single_len, pattern_len = 2, 3
    while i <= len(split_tokens)-single_len:
        forward1 = concat(split_tokens[i:i+single_len])
        forward2 = concat(split_tokens[i:i+pattern_len])

        if is_segment_pattern([forward2]):
            results.append(forward2)
            i += pattern_len
        elif is_variable(forward1):
            results.append(forward1)
            i += single_len
        else:
            results.append(split_tokens[i])
            i += 1

    if i == len(split_tokens) - 1:
        results.append(split_tokens[-1])

    return results


def cut(string):
    return merge_variable(list(jieba.cut(string)))


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
    # while True:
        # sentence = input('USER >>>')
        sentence = '小哥哥我想要你做我的男朋友'
        match = eliza(sentence)
        # if match:
        print(''.join(compose_single_sentene(match)))
        # else:
        #     print('sorry I don\'t know it')



