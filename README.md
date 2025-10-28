📘 Projeto: Processamento de Imagem em Texto com Python

Este projeto demonstra, de forma simplificada, como funciona o processamento de imagens em Python — sem usar bibliotecas externas, sem plugins e utilizando apenas recursos básicos da linguagem.

A imagem usada no exemplo não é um arquivo .jpg ou .png, mas sim um arquivo de texto (minha_imagem.txt) contendo valores RGB, simulando uma imagem 3×3 pixels.

O script processar.py realiza três etapas principais:

📥 Carregamento da imagem a partir de um arquivo .txt

🎨 Conversão para Tons de Cinza

⚫⚪ Binarização (Preto e Branco)

📂 Estrutura dos Arquivos
📁 projeto/
 ├── processar.py
 ├── minha_imagem.txt
 └── README.md  ← (este arquivo)


🧾 Formato do Arquivo de Imagem (minha_imagem.txt)

Cada pixel é representado por R,G,B, e cada linha representa uma linha da imagem:

255,0,0 0,255,0 0,0,255
255,255,0 0,255,255 255,0,255
255,255,255 128,128,128 0,0,0


✅ 3 linhas → altura
✅ 3 valores por linha → largura
✅ Cada valor → um pixel da imagem

🧠 Funcionamento do Código
✅ 1️⃣ Leitura da Imagem

O Python abre o arquivo texto e converte cada valor para uma lista 3D:

imagem_rgb = [
    [[255,0,0], [0,255,0], [0,0,255]],
    [[255,255,0], [0,255,255], [255,0,255]],
    [[255,255,255], [128,128,128], [0,0,0]]
]


📌 Esse formato é equivalente a uma matriz de pixels em memória.

🌓 2️⃣ Conversão para Tons de Cinza

Cada pixel RGB é convertido para um único valor de intensidade luminosa:

Fórmula utilizada (padrão NTSC)

Cinza = 0.299*R + 0.587*G + 0.114\*B

Exemplo:

Pixel vermelho puro (255,0,0) → 76

Pixel branco (255,255,255) → 255

Pixel preto (0,0,0) → 0

Resultado: imagem se torna uma matriz 2D.

⚪⚫ 3️⃣ Binarização (Preto e Branco)

Aplica-se um limiar (128) para decidir:

Pixel Cinza > 128 Resultado
✅ Branco (255)
❌ Preto (0)

Assim, a imagem passa a conter apenas dois valores.

▶️ Como Executar

No terminal, dentro da pasta do projeto:

python3 processar.py

Quando solicitado, digite:

minha_imagem.txt

🧩 Objetivo Pedagógico

Este código permite compreender:

✅ Como uma imagem é representada numericamente
✅ Como manipular os valores dos pixels
✅ Como funcionam as etapas básicas de processamento de imagem:

Representação RGB

Tons de Cinza

Limiarização

Sem depender de bibliotecas como OpenCV ou PIL — ideal para aprendizado inicial.

👨‍💻 Autor

Sandro Paiva
Projeto criado para fins de estudo em Python e processamento de imagem.
