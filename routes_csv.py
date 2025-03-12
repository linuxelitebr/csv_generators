import os
import csv
import re

pasta_txt = "apps-detail"
saida_csv = "rotas.csv"

dados = []

for arquivo in os.listdir(pasta_txt):
    if arquivo.endswith(".txt"):
        namespace = arquivo.replace(".txt", "")
        caminho_arquivo = os.path.join(pasta_txt, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                
                if linha.startswith("route.route.openshift.io/"):
                    partes = re.split(r'\s{2,}', linha)

                    dados.append([namespace] + partes)

with open(saida_csv, "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerows(dados)

print(f"Arquivo CSV '{saida_csv}' gerado com sucesso! Total de rotas processadas: {len(dados)}")
