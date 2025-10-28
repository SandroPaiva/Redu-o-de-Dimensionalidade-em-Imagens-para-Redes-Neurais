# --- Parte 1: Carregar a Imagem ---

# A única função "não pura" que usaremos é a 'open' e 'input', 
# que são embutidas (built-in) do Python.
# Elas são necessárias para ler *qualquer* arquivo.

imagem_rgb = [] # A lista 3D final
nome_arquivo = ""

try:
    # 1. Perguntar ao usuário qual "imagem" carregar nesse exemplo, 
    nome_arquivo = input("Digite o nome do arquivo de imagem (.txt): ")
    
    # 2. Abrir o arquivo de texto para leitura ('r')
    with open(nome_arquivo, 'r') as f:
        
        # 3. Ler linha por linha
        for linha_texto in f.readlines():
            
            nova_linha_pixels = []
            
            # Limpa espaços em branco no início/fim da linha
            linha_texto_limpa = linha_texto.strip()
            
            # Se a linha não estiver vazia
            if linha_texto_limpa:
                
                # 4. Quebra a linha nos espaços (cada parte é um pixel)
                pixels_como_texto = linha_texto_limpa.split(' ')
                
                for pixel_texto in pixels_como_texto:
                    # 5. Quebra o pixel nas vírgulas (R, G, B)
                    valores_rgb_texto = pixel_texto.split(',')
                    
                    # 6. Converte os valores de texto para números inteiros
                    r = int(valores_rgb_texto[0])
                    g = int(valores_rgb_texto[1])
                    b = int(valores_rgb_texto[2])
                    
                    # Adiciona o pixel [R,G,B] à nossa linha
                    nova_linha_pixels.append([r, g, b])
            
            # Adiciona a linha de pixels à imagem final
            if nova_linha_pixels:
                imagem_rgb.append(nova_linha_pixels)
    print(f"--- Imagem '{nome_arquivo}' carregada com sucesso! ---")
    print("Imagem RGB Original (como lista 3D):")
    print(imagem_rgb)


    # --- Parte 2: Transformar para Tons de Cinza ---
    
    imagem_cinza = []
    for linha_pixels in imagem_rgb:
        nova_linha_cinza = []
        for pixel in linha_pixels:
            r, g, b = pixel[0], pixel[1], pixel[2]
            valor_cinza = int( (0.299 * r) + (0.587 * g) + (0.114 * b) )
            nova_linha_cinza.append(valor_cinza)
        imagem_cinza.append(nova_linha_cinza)

    print("\n--- Imagem em Tons de Cinza (lista 2D): ---")
    for linha in imagem_cinza:
        print(linha)


    # --- Parte 3: Transformar para Binarizado  ---

    limiar = 128
    imagem_binaria = []

    for linha_cinza in imagem_cinza:
        nova_linha_binaria = []
        for pixel_cinza in linha_cinza:
            if pixel_cinza > limiar:
                nova_linha_binaria.append(255) # Branco
            else:
                nova_linha_binaria.append(0)   # Preto
        imagem_binaria.append(nova_linha_binaria)

    print("\n--- Imagem Binarizada (lista 2D): ---")
    for linha in imagem_binaria:
        print(linha)


except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")