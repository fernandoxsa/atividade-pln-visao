# Atividade de PLN e Visão Computacional

Este projeto contém dois exemplos práticos desenvolvidos em Python com base nos conteúdos apresentados nas aulas de Processamento de Linguagem Natural (PLN) e Visão Computacional.

## Exemplo 1: Processamento de Linguagem Natural

### Técnica utilizada
Tokenização e remoção de stop-words.

### Biblioteca
NLTK (Natural Language Toolkit).

### Descrição
O script lê um texto em português, converte para letras minúsculas, realiza a tokenização para dividir o texto em palavras e depois remove as palavras de alta frequência (stop-words). O objetivo é limpar o texto para permitir outras análises.

### Execução
Instale as dependências com:
```bash
python3 -m pip install nltk
```
Execute o script:
```bash
python3 exemplo_1_pln.py
```

O programa exibe o texto original, a lista de tokens gerados e os tokens restantes após a remoção das stop-words.

## Exemplo 2: Visão Computacional

### Técnica utilizada

Equalização de histograma.

### Biblioteca

OpenCV e Matplotlib.

### Descrição

O script lê uma imagem em escala de cinza (imagem_teste.jpg), aplica a equalização de histograma para melhorar o contraste, salva a imagem resultante em resultado_equalizado.jpg e exibe, em uma figura, a comparação entre a imagem original e a imagem equalizada.

### Execução

Instale as dependências com:
```bash
python3 -m pip install opencv-python matplotlib
```
Execute o script:
```bash
python3 exemplo_2_visao.py
```

Certifique-se de ter uma imagem chamada imagem_teste.jpg no mesmo diretório. Após a execução, será criado o arquivo resultado_equalizado.jpg e uma janela mostrará a imagem original e a equalizada.

## Estrutura do projeto
```
atividade-pln-visao/
├── exemplo_1_pln.py
├── exemplo_2_visao.py
├── imagem_teste.jpg
├── resultado_equalizado.jpg
├── README.md
└── prints/
    ├── print_pln_terminal.png
    ├── print_visao_terminal.png
    └── print_visao_resultado.png
```

## Instalação das dependências
```bash
python3 -m pip install nltk opencv-python matplotlib
```

## Autor

José Fernando Gonçalves de Sá Filho