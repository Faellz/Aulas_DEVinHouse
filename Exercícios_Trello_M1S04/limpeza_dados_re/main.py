'''Crie um script que receba uma lista de e-mails e utilize o módulo re para:
Identificar e-mails válidos.
Separar os inválidos em outro arquivo.
Entrega: Script .py e dois arquivos .txt (válidos e inválidos).'''

import re

normal_mail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

with open("email_aleatorios.txt", "r", encoding="utf-8") as arquivo:
    emails = arquivo.read().splitlines()

emails_validos = []
emails_invalidos = []

for email in emails:
    if re.match(normal_mail, email):
        emails_validos.append(email)
    else:
        emails_invalidos.append(email)

with open("emails_validos.txt", "w", encoding="utf-8") as arquivo_validos:
    for email in emails_validos:
        arquivo_validos.write(email + "\n")


with open("emails_invalidos.txt", "w", encoding="utf-8") as arquivo_invalidos:
    for email in emails_invalidos:
        arquivo_invalidos.write(email + "\n")

