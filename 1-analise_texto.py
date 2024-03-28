import os
import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.probability import FreqDist
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

nltk.download('punkt')

# 1 - Importação do Texto
with open(os.path.join("data", "texto.txt"), "r", encoding="utf-8") as file:
    texto = file.read()
    print(texto)
    
# 2 - Tokenizando o Texto
sent_tokens = sent_tokenize(texto)
print(sent_tokens)
print(len(sent_tokens))

word_tokens = word_tokenize(texto)
print(word_tokens)
print(len(word_tokens))

# 3 - Frequência de Distribuição
fdist = FreqDist(word_tokens)
# print(fdist)
print(fdist.most_common(10))
# fdist.plot(10)    #gera imagem de estatística

# 4 - WordCloud /  WordCloud Customizado
def plot_cloud(wordcloud):
    plt.figure(figsize=(40,30))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color= 'salmon',
    colormap = 'Pastel1',
    collocations = False,
    stopwords = STOPWORDS
).generate(texto)

# plot_cloud(wordcloud)  #gera imagem de Word Cloud

mascara = np.array(
    Image.open("data/upvote.png")
)

wordcloud = WordCloud(
    width = 3000,
    height = 2000,
    random_state = 1,
    background_color= 'salmon',
    colormap = 'Pastel1',
    collocations = False,
    stopwords = STOPWORDS,
    mask = mascara
).generate(texto)
plot_cloud(wordcloud)  #gera imagem de Word Cloud
