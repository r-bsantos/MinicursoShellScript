import sys

# Verifica se um nome de arquivo foi passado no terminal
if len(sys.argv) < 2:
    print("Erro: Você precisa informar o nome do arquivo texto.")
    sys.exit(1)

nome_arquivo = sys.argv[1]

try:
    # Tenta abrir o arquivo enviado pelo Shell Script
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

        # Conta letras e palavras
        qtd_caracteres = len(conteudo)
        qtd_palavras = len(conteudo.split())

        # Retorna o resultado para o Shell
        print(f" -> [Python Processou] {nome_arquivo}: {qtd_palavras} palavras e {qtd_caracteres} caracteres totais.")

except FileNotFoundError:
    print(f" -> [Python Erro] O arquivo '{nome_arquivo}' não foi encontrado.")
