import os

caminhos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
jpgs = [arq for arq in arquivos if arq.lower().endswith('.jpg')]

print(caminhos)
print(arquivos)
print(jpgs)