from goose3 import Goose
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

# 1 - coletando o artigo
g = Goose()
url = 'https://olhardigital.com.br/2024/02/28/pro/drex-moeda-digital-esta-praticamente-pronta-mas-lancamento-pode-atrasar/'
noticia = g.extract(url)
# print(noticia.cleaned_text)

# 2 - Trabalhando com a sumarização
parser = PlaintextParser.from_string(
    noticia.cleaned_text,
    Tokenizer('portuguese')
)

sumarizador = LuhnSummarizer()

resumo = sumarizador(
    parser.document,
    2
)

for sentenca in resumo:
    print(sentenca)