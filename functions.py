from pyexpat import features

from camel_tools.utils.charmap import CharMapper
from camel_tools.utils.transliterate import Transliterator
from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer
from camel_tools.morphology.generator import Generator
import random
from wordlist import *
import wordlist

bw2ar = CharMapper.builtin_mapper('bw2ar')
bw2ar_translit = Transliterator(bw2ar)

sentence_bw = 'ktb'
sentence_ar = bw2ar_translit.transliterate(sentence_bw)
sentence_ar_stripped = bw2ar_translit.transliterate(sentence_ar, strip_markers=True)

dba = MorphologyDB.builtin_db()
dbg = MorphologyDB.builtin_db(flags="g")

analyzer = Analyzer(dba, "NOAN_PROP")
generator = Generator(dbg)

def pickword():
    return random.choice(list(words.keys()))

def pickform():
    forms = [
        ('3', 'm', 's', 'p'),
        ('3', 'm', 'd', 'p'),
        ('3', 'm', 'p', 'p'),
        ('3', 'f', 's', 'p'),
        ('3', 'f', 'd', 'p'),
        ('3', 'f', 'p', 'p'),
        ('2', 'm', 's', 'p'),
        ('2', 'm', 'd', 'p'),
        ('2', 'm', 'p', 'p'),
        ('2', 'f', 's', 'p'),
        ('2', 'f', 'd', 'p'),
        ('2', 'f', 'p', 'p'),
        ('1', 'm', 's', 'p'),
        ('1', 'm', 'p', 'p'),
        ('3', 'm', 's', 'i'),
        ('3', 'm', 'd', 'i'),
        ('3', 'm', 'p', 'i'),
        ('3', 'f', 's', 'i'),
        ('3', 'f', 'd', 'i'),
        ('3', 'f', 'p', 'i'),
        ('2', 'm', 's', 'i'),
        ('2', 'm', 'd', 'i'),
        ('2', 'm', 'p', 'i'),
        ('2', 'f', 's', 'i'),
        ('2', 'f', 'd', 'i'),
        ('2', 'f', 'p', 'i'),
        ('1', 'm', 's', 'i'),
        ('1', 'm', 'p', 'i')
    ]
    return random.choice(forms)

def generate_conjugations(sentence_bw, person, gender, number, tense):
    wordlist = []
    sentence_ar = bw2ar_translit.transliterate(sentence_bw)
    sentence_ar_stripped = bw2ar_translit.transliterate(sentence_ar, strip_markers=True)

    ar_word = sentence_ar_stripped
    analysed_words = analyzer.analyze(ar_word)

    for analysis in analysed_words:
        if analysis['pos'] == 'verb':
            lemma = analysis['lex']
            break


    features = {
        'pos': 'verb',
        'asp': tense,
        'per': person,
        'num': number,
        'gen': gender
    }

    generated = generator.generate(lemma, features)

    if generated:
        wordlist.append(generated[0]['diac'])

    return wordlist



