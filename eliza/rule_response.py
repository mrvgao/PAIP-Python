from eliza.pattern_match import sub_list
from eliza.pattern_match import pattern_match_l
from eliza.pattern_match import fail
import random
from eliza.rules import rule_responses
from utilities import cut
from utilities import concat


def get_rule(rule_string_format):
    return {
        # tuple(k.split()): [line.split() for line in v]
        tuple(cut(k)): [cut(line) for line in v]
        for k, v in rule_string_format.items()
    }


def eliza(speech):
    # speech = speech.split()
    speech = cut(speech)

    for index, (pattern, responses) in enumerate(get_rule(rule_responses).items()):
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
            print('{:>40}<<<'.format(concat(compose_single_sentene(match))))
        else:
            print('sorry I don\'t know it')



