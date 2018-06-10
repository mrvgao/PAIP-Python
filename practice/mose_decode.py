code_source = """.-.-....-.-...--.-...-....--...-.-...-.--.------..-...-..-.-.---...-..-..---..-..

....--..-.--.-...-.--......-.........-..-.----.-.....-....--.-.-.--.-..---..-....

..-...-..-.--.-.----......-.--.-----..-------.-.-..---.-.-.--..-.-...............

--...--....--..-....-.-----.....-...-------.-......-.........-..-..--.-....-...--

....-.--.-.....--..-.....--..-.---.--...-.-.-..-.-.....---.-.-.-.----....-..-....

.--..----......-...-.--.-...--.....--.....-.......-....---..-..--...-------.--...

.---..---.....-.-.-....-.-...--..-....---..--.--...-.-.-..-.-.....---.-.-.-.----.

...-..-.....--..----."""

code_source = ''.join(code_source.split())

morse_alphabet = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}

morse_abc_map = {m: c for c, m in morse_alphabet.items()}


def split_long_code(src_code, myopia=True):
    if len(src_code) == 0: return []

    for i in range(len(src_code)):
        if (myopia and src_code[:i] in morse_abc_map) or (
                not myopia and src_code[:i] in morse_abc_map and src_code[:i + 1] not in morse_abc_map):
            return [morse_abc_map[src_code[:i]]] + split_long_code(src_code[i:])
    return []


print(split_long_code(code_source))
print(split_long_code(code_source, myopia=False))

morse_word_map = {}
word_morse_map = {}


def map_english_to_morse(vocab):
    for w in vocab:
        morse_code = ''.join(morse_abc_map[c] for c in w)
        morse_abc_map[morse_code] = w
        word_morse_map[w] = morse_code
