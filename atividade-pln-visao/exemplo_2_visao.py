import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("imagem_teste.jpg", cv2.IMREAD_GRAYSCALE)

if imagem is None:
    print("Erro: não foi possível carregar a imagem.")
else:
    imagem_equalizada = cv2.equalizeHist(imagem)
    cv2.imwrite("resultado_equalizado.jpg", imagem_equalizada)

    print("=== EXEMPLO 2: VISÃO COMPUTACIONAL ===")
    print("Imagem carregada com sucesso.")
    print("Equalização de histograma aplicada.")
    print("Resultado salvo como: resultado_equalizado.jpg")

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Imagem Original")
    plt.imshow(imagem, cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Imagem Equalizada")
    plt.imshow(imagem_equalizada, cmap="gray")
    plt.axis("off")

    plt.show()