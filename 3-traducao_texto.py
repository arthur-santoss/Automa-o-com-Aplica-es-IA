from deep_translator import GoogleTranslator

# 1 - idiomas disponiveis
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
# print(langs_dict)

# 2 - tradução de PT para EN
text = 'Estamos estudando PLN (Processamento de Linguagem Natural)'
translated = GoogleTranslator(
    source= 'pt',
    target= 'en'
).translate(text=text)

print(translated)

# 3 - tradução em itens de uma lista
texts = [
    "Estou aprendendo automação com Python",
    "Estou gostando muito",
    "Quero aprender a desenvolver sistemas em Python"
]
translated_itens = GoogleTranslator(
    source = 'pt',
    target = 'en'
).translate_batch(texts)
print(translated_itens)