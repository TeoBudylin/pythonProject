import goslate

# gs = goslate.Goslate()
# print(gs.translate('hello world', 'ru'))

# import googletrans
# translator = googletrans.Translator()

# from googletrans import Translator
#
# with open("4.txt", "r",  encoding='utf-8') as f:
#     with open("4_1.txt", "w",  encoding='utf-8') as f2:
#         for line in f:
#             # f2.write(gs.translate(line, "ru"))
#             t = Translator()
#             a = t.translate(line)
#             print(a)

# from googletrans import Translator
# with open('4_1.txt', 'w', encoding='utf-8') as nf:
#     with open('4.txt', 'r', encoding='utf-8') as mf:
#         text = mf.read()
#     t = Translator()
#     a = t.translate(text)
#     print(a)

rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('4_1.txt', 'w', encoding='utf-8') as nf:
    with open('4.txt', 'r', encoding='utf-8') as mf:
        nf.write(str([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in mf]))

