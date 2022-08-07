from googletrans import Translator

def translate(text):
    translator = Translator()
    translation = translator.translate(text=text, dest='zh-cn')
    return translation.text
