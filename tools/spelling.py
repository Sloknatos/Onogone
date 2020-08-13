from spellchecker import SpellChecker
import fr_core_news_sm
import re
from tools.convert_number import convert_number

spell = SpellChecker(language='fr')
npl = fr_core_news_sm.load()


def remplace(sentence):
    doc = npl(sentence)
    temp = ""
    for word in doc:
        if word.pos_ == "PUNCT":
            temp += word.text
        elif word.pos_ == "DET":
            temp += " " + word.text
        elif word.pos_ == "VERB" or word.pos_ == "AUX":
            temp += " " + word.lemma_
        elif word.text.isdigit():
            temp += " " + convert_number(word.text)
        else:
            temp += " " + word.lemma_
    return temp


def respelling(sentence):
    doc = npl(sentence)
    pattern = re.compile(r'\'|(|)')
    for word in doc:
        if re.match(pattern, word.text):
            continue
        if word.pos_ == "NOUN" or word.pos_ == "VERB":
            sentence = re.sub(word.text, spell.correction(word.text), sentence)
    return remplace(sentence)
