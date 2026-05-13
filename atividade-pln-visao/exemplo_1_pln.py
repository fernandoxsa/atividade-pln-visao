import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")

texto = """
O Processamento de Linguagem Natural permite que computadores compreendam,
interpretem e processem a linguagem humana em diversas aplicações,
como chatbots, tradutores automáticos e análise de sentimentos.
"""

texto_minusculo = texto.lower()

tokens = word_tokenize(texto_minusculo, language="portuguese")

stop_words = set(stopwords.words("portuguese"))

tokens_filtrados = [
    palavra for palavra in tokens
    if palavra.isalpha() and palavra not in stop_words
]

print("=== EXEMPLO 1: PLN ===")

print("\nTexto original:")
print(texto)

print("\nTokens gerados:")
print(tokens)

print("\nTokens após remoção de stop-words:")
print(tokens_filtrados)