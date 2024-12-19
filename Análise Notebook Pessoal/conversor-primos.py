import os
import csv

# Função para criar os titulos das colunas
def agrupar_txt_para_csv(pasta, arquivo_csv):
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        arquivos_processados = 0  # Contador
        linhas_processadas = set()

        for nome_arquivo in os.listdir(pasta):
            # Verifica se é um arquivo .txt
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            if os.path.isfile(caminho_arquivo) and nome_arquivo.endswith('.txt'):
                print(f"Lendo o arquivo: {nome_arquivo}")

                # Lê o conteúdo do arquivo
                with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                    linhas = file.readlines()

                for linha in linhas:
                    # Divide a linha em palavras (separadas por tabulação ou espaços)
                    partes = linha.split()

                    if len(partes) >= 5:  # Garante que a linha tem pelo menos 5 colunas
                        # Extrai as 5 primeiras informações
                        palavras = tuple(partes[:5])
                        
                        if palavras not in linhas_processadas:  # Verifica se a linha já foi processada
                            writer.writerow(palavras)  # Escreve a linha no CSV
                            linhas_processadas.add(palavras)  # Marca a linha como processada
                            arquivos_processados += 1
                    else:
                        print(f"A linha não contém 5 partes: {linha}")

        # Verifica se algum arquivo foi processado
        if arquivos_processados == 0:
            print("Nenhuma linha única foi processada e gravada no CSV.")
        else:
            print(f"{arquivos_processados} linhas únicas foram processadas e gravadas no CSV.")

# Exemplo de uso
pasta_dos_arquivos = r'C:\Users\bruns\Downloads\ADS-Lab1\output-bench-primos/'  # Substitua com o do seu
arquivo_csv = 'Análise Notebook Pessoal/dataset-primos.csv'  # Nome do arquivo CSV que será gerado

agrupar_txt_para_csv(pasta_dos_arquivos, arquivo_csv)
