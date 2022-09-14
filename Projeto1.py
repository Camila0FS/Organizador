# Programa 1 - Organizador
# Descrição:
# Este programa organiza os arquivos nas pastas planilhas e documentos.

# Autor: Camila Freitas Sant Ana
# Versão: 0.0.5 # Data: 30/08/2022

# Anotações: Arquivos: • orcamento.xls • orcamento.docx • clientes.xls  • clientes.doc • relatorio.doc

# Abrir terminal - via jupiter notebook
# C:\Users\Users> cd projeto1
# C:\Users\Users\projeto1> ls (listou os arquivos)

# no jupiter notebook new ipykernel - renomeado Projeto1.py

import os

# Criando diretórios

if os.path.exists('documentos') == False:
    os.mkdir('documentos')
    
if os.path.exists('planilhas') == False:
    os.mkdir('planilhas')
    
# após conferência se não existe a pasta planilha e documentos o comando anterior irá criar no diretório onde encontram-se os arquivos

# pelo comando do terminal usar o touch para criar os arquivos - • orcamento.xls • orcamento.docx • clientes.xls  • clientes.doc • relatorio.doc

# C:\Users\Users\projeto1> touch orcamento.xls

# C:\Users\Users\projeto1> touch orcamento.docx

# C:\Users\Users\projeto1> touch clientes.xls

# C:\Users\Users\projeto1> touch clientes.doc

# C:\Users\Users\projeto1> touch relatorio.doc

# posteriormente mover os arquivos para suas respectivas pastas pelo jupiter notebook Projeto1.py


import shutil
import os

arquivos = os.listdir()

for arquivo in arquivos:
    if ".xls" in arquivo:
        shutil.move(arquivo, f"./planilhas/{arquivo}")
    elif ".doc" in arquivo:
        shutil.move(arquivo, f"./documentos/{arquivo}")
    elif ".docx" in arquivo:
        shutil.move(arquivo, f"./documentos/{arquivo}")   
        
import os
lista = os.listdir()
print(lista)









