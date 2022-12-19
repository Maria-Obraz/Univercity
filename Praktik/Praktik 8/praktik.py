import re
import pymorphy2
from translate import Translator
import translate

def read_file(filename: str):
    f = open(filename, 'r', encoding='utf-8')
    wor = f.read()
    wor = re.sub(r'[^\w\s]', '', wor)
    wor = re.sub(r"\d+", '', wor)
    return wor.split()

def list_words(worrds: [str]):
    worrdsCount = {}

    for wor in worrds:
        if len(wor) > 1:
            if not wor in worrdsCount:
                worrdsCount[wor] = 0
            worrdsCount[wor] += 1

    sorted_worrds = {}
    sorted_keys = sorted(worrdsCount, key=worrdsCount.get)
    sorted_keys.reverse()

    for values in sorted_keys:
        sorted_worrds[values] = worrdsCount[values]

    return sorted_worrds

def translate(worrds: {}):
    morph = pymorphy2.MorphAnalyzer()
    translator = Translator(from_lang="ru", to_lang="en")

    translate_worrds = {}
    for key, value in worrds.items():
        en_worrd = str
        try:
            normal_worrd = morph.parse(key)[0].normal_form
            en_worrd = translator.translate(normal_worrd)
            if en_worrd == None:
                raise Exception
        except:
            en_worrd = 'untranslated'

        print(en_worrd)
        translate_worrds[en_worrd] = value

    return translate_worrds


def write_file(filename, translate_words: {}, sorted_words: {}):
    ru_words = []
    en_words = []
    words_count = []

    for key, value in sorted_words.items():
        ru_words.append(key)

    for key, value in translate_words.items():
        en_words.append(key)
        words_count.append(value)

    f = open(filename, 'a')
    for i in range(len(translate_words)):
        line = "{0} - {1} {2} \n".format(en_words[i], ru_words[i], words_count[i])
        f.write(line)

words = read_file('dialog.txt')
sorted_words = list_words(words)
transleted_words = translate(sorted_words)
write_file('TranslatedWords.txt', transleted_words, sorted_words)