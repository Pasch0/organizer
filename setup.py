#!/usr/bin/python3
import subprocess as sp

# Apresentação e assinatura
signature = (
    "\n   ____                        _              "
    "\n  / __ \                      (_)             "
    "\n | |  | |_ __ __ _  __ _ _ __  _ _______ _ __ "
    "\n | |  | | '__/ _` |/ _` | '_ \| |_  / _ \ '__|"
    "\n | |__| | | | (_| | (_| | | | | |/ /  __/ |   "
    "\n  \____/|_|  \__, |\__,_|_| |_|_/___\___|_|   "
    "\n              __/ |                           "
    "\n             |___/                  by Pasch0\n\n"
)

print(signature)

# Mensagem de confirmação de execução com permissões adequadas
disclaimer = (
    "\n\nAttention: To work correctly, this script needs to be executed as follows: \n"
    "$ python3 setup.py"
    "\nIf you have not done so, quit and rerun."
)
print(disclaimer)
confirm = input("\nDo you want to proceed(Y/n)? ")

# Lista de variações a serem verificadas
positive = ["y", "yes", ""]
negative = ["n", "no"]
run = False

# Verificação de resposta positiva do usuário
for answer in positive:
    if confirm.lower() == answer:
        run = True

# Verificação de resposta negativa do usuário
for answer in negative:
    if confirm.lower() == answer:
        sp.call("clear")
        print(signature)
        print("Please run this script as follows:\n" "$ python3 setup.py")

# Copia o script para a pasta /usr/bin e adiciona comandos ao .bashrc
def copy_to_bin():
    # Copia o script
    sp.call(["sudo", "cp", "organizer.py", "/usr/bin/"])
    # Permite a execução do script que atualiza o .bashrc
    sp.call(["sudo", "chmod", "+x", "bashupdate.sh"])
    # Adiciona os comandos ao .bashrc
    sp.call(["./bashupdate.sh"])


if run == True:
    copy_to_bin()
