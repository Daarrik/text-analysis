from googletrans import Translator
from urllib.parse import urljoin

base = 'https://en.wikipedia.org/wiki/Yugoslav_gunboat_Beli_Orao'
sub = '/wiki/Galeb-class_minelayer'
print(urljoin(base, sub))


translator = Translator()
print(translator.detect('test').lang)