from camel_tools.utils.charmap import CharMapper
from camel_tools.utils.transliterate import Transliterator
from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer
from camel_tools.morphology.generator import Generator

bw2ar = CharMapper.builtin_mapper('bw2ar')
bw2ar_translit = Transliterator(bw2ar)

sentence_bw = 'ktb'
sentence_ar = bw2ar_translit.transliterate(sentence_bw)
sentence_ar_stripped = bw2ar_translit.transliterate(sentence_ar, strip_markers=True)

dba = MorphologyDB.builtin_db()
dbg = MorphologyDB.builtin_db(flags="g")

analyzer = Analyzer(dba, "NOAN_PROP")
generator = Generator(dbg)

def generate_conjugations(sentence_bw,tense,voice):
    wordlist = []
    sentence_ar = bw2ar_translit.transliterate(sentence_bw)
    sentence_ar_stripped = bw2ar_translit.transliterate(sentence_ar, strip_markers=True)

    ar_word = sentence_ar_stripped
    analysed_words = analyzer.analyze(ar_word)

    for analysis in analysed_words:
        if analysis['pos'] == 'verb':
            lemma = analysis['lex']
            break

    forms = [
        ('3', 'm', 's'),
        ('3', 'm', 'd'),
        ('3', 'm', 'p'),
        ('3', 'f', 's'),
        ('3', 'f', 'd'),
        ('3', 'f', 'p'),
        ('2', 'm', 's'),
        ('2', 'm', 'd'),
        ('2', 'm', 'p'),
        ('2', 'f', 's'),
        ('2', 'f', 'd'),
        ('2', 'f', 'p'),
        ('1', 'm', 's'),
        ('1', 'm', 'p')
    ]

    for person, gender, number in forms:

        features = {
            'pos': 'verb',
            'asp': tense,
            'vox': voice,
            'per': person,
            'gen': gender,
            'num': number
        }

        generated = generator.generate(lemma, features)

        if generated:
            wordlist.append(generated[0]['diac'])

    return wordlist

print(generate_conjugations('ftH','p', 'a')) 