from camel_tools.utils.charmap import CharMapper
from camel_tools.utils.transliterate import Transliterator
from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.analyzer import Analyzer
from camel_tools.morphology.generator import Generator
from camel_tools.utils.dediac import dediac_ar
from camel_tools.morphology.reinflector import Reinflector
from sympy.physics.optics import lens_makers_formula

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
# print(analysed_words[1]['lex'])
# lemma = analysed_words[1]['lex']
# features = {
#     'pos': 'verb',
#     'gen': 'm',
#     'asp': 'i',
#     'per': '1',
#     'num': 's',
#     'vox': 'a'
# }
#
# # Generate analyses for lemma and features
# generated = generator.generate(lemma, features)
# for i in generated:
#     print(i["diac"])
new_feats = {
    'asp': 'p',
    'per': '3',
    'gen': 'm',
    'num': 's',
    'vox': 'a'
}
analysis = analysed_words[0]
print(analysis)
reinflector = Reinflector(dbr)
reinflected = reinflector.reinflect(analysis['diac'], new_feats)
print([g['diac'] for g in reinflected])

# print(f"analysis is{analyses}")
