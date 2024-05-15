from googletrans import Translator

def translate_to_turkish(word):
    translator = Translator()
    translation = translator.translate(word, src='en', dest='tr')
    return translation.text

def translate_to_english(word):
    translator = Translator()
    translation = translator.translate(word, src='tr', dest='en')
    return translation.text

value=int(input("Value>>"))
if value == 1 :
    word=input(">>")
    turkish_translation = translate_to_turkish(word)
    print("Turkish Translation:", turkish_translation)
else:
    word=input(">>")
    english_translation = translate_to_english(word)
    print(f"English Translation:{english_translation}")

