from camel_tools.utils.charmap import CharMapper
from camel_tools.utils.transliterate import Transliterator
from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer
from camel_tools.morphology.generator import Generator
from camel_tools.utils.dediac import dediac_ar
from camel_tools.morphology.reinflector import Reinflector

bw2ar = CharMapper.builtin_mapper('bw2ar')
bw2ar_translit = Transliterator(bw2ar)

sentence_bw = 'ktb'
sentence_ar = bw2ar_translit.transliterate(sentence_bw)
sentence_ar_stripped = bw2ar_translit.transliterate(sentence_ar, strip_markers=True)

print('Original sentence:\n\t', sentence_bw)
print('Buckwalter encoded sentence:\n\t', sentence_ar)
print('Buckwalter encoded sentence + stripped markers:\n\t', sentence_ar_stripped)

dba = MorphologyDB.builtin_db()
dbg = MorphologyDB.builtin_db(flags="g")
dbr = MorphologyDB.builtin_db(flags="r")

analyzer = Analyzer(dba, "NOAN_PROP")
analyses = analyzer.analyze('مفتاح')

# for diac in set([a['diac'] for a in analyses]):
#     print(diac)
#
generator = Generator(dbg)


ar_word = sentence_ar_stripped
analysed_words = analyzer.analyze(ar_word)

for analysis in analysed_words:
    if analysis['pos'] == 'verb':
        lemma = analysis['lex']
        break

wordlist = []

forms = [
    ('هُوَ',     '3', 'm', 's'),
    ('هُمَا',    '3', 'm', 'd'),
    ('هُمْ',     '3', 'm', 'p'),
    ('هِيَ',     '3', 'f', 's'),
    ('هُمَا',    '3', 'f', 'd'),
    ('هُنَّ',    '3', 'f', 'p'),
    ('أَنْتَ',   '2', 'm', 's'),
    ('أَنْتُمَا','2', 'm', 'd'),
    ('أَنْتُمْ', '2', 'm', 'p'),
    ('أَنْتِ',   '2', 'f', 's'),
    ('أَنْتُمَا','2', 'f', 'd'),
    ('أَنْتُنَّ','2', 'f', 'p'),
    ('أَنَا',    '1', 'm', 's'),
    ('نَحْنُ',   '1', 'm', 'p')
]

for pronoun, person, gender, number in forms:

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

print(wordlist)