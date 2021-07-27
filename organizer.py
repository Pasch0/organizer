# Importar módulo subprocess que permite executar comandos do SO
import subprocess as sp

# Importar módulo time
from time import sleep

# Criar listas categorizando cada tipo de arquivo a ser organizado
compactados = (".zip", ".tar", ".rar", ".gz", ".bz")
imagens = (".png", ".jpg", ".jpeg", ".svg")
videos = (".mp4", ".mov", ".webm", ".kmv")
musicas = (".mp3", ".wav", ".mpeg3")
desenvolmimento = (".py", ".php", ".html", ".json", ".css", ".js")
executaveis = (".exe", ".sh", ".deb", ".appimage")
texto = (".txt", ".pdf", ".odt")

# Pastas a serem criadas caso não existam
diretorios = [
    "compactados",
    "imagens",
    "videos",
    "musicas",
    "desenvolvimento",
    "executaveis",
    "texto",
]

# Caminho da(s) pasta(s) a ser(em) monitorada(s)
pasta_monitorada = "/home/pasch0/Downloads/"  # Substitua pela sua pasta monitorada

# Caminho para a pasta do organizador
organizer_path = (
    "/home/pasch0/Downloads/organizer/"  # Substitua para a pasta do organizador
)

# Nomes dos arquivos encontrados na(s) pasta(s) serão armazenados aqui
arquivos = []

# Stop do laço de repetição
stop = ["1"]

# Captura de conteúdo da(s) pasta(s) monitorada(s)
def listar_arquivos():
    ls = sp.Popen(["ls", pasta_monitorada], stdout=sp.PIPE)
    listagem = ls.stdout.readlines()
    for arquivo in listagem:
        arquivos.append(arquivo.decode("ascii").rstrip())


# Cria pastas para o armazenamento organizado
def criar_diretorios():
    mkdir = sp.call(["mkdir", organizer_path], stdout=None)
    for diretorio in diretorios:
        mkdir = sp.call(["mkdir", organizer_path + diretorio])


# Move os arquivos para suas respectivas pastas
def mover_arquivos():
    for arquivo in arquivos:
        if arquivo.endswith(texto):
            comando = ["mv", pasta_monitorada + arquivo, organizer_path + diretorios[6]]
            mv = sp.Popen(comando)
        elif arquivo.endswith(executaveis):
            comando = ["mv", pasta_monitorada + arquivo, organizer_path + diretorios[5]]
            mv = sp.Popen(comando)
        elif arquivo.endswith(desenvolmimento):
            comando = ["mv", pasta_monitorada + arquivo, organizer_path + diretorios[4]]
            mv = sp.Popen(comando)
        elif arquivo.endswith(musicas):
            comando = ["mv", pasta_monitorada + arquivo, organizer_path + diretorios[3]]
            mv = sp.Popen(comando)
        elif arquivo.endswith(videos):
            comando = ["mv", pasta_monitorada + arquivo, organizer_path + diretorios[2]]
            mv = sp.Popen(comando)
        elif arquivo.endswith(imagens):
            comando = ["mv", pasta_monitorada + arquivo, organizer_path + diretorios[1]]
            mv = sp.Popen(comando)
        elif arquivo.endswith(compactados):
            comando = ["mv", pasta_monitorada + arquivo, organizer_path + diretorios[0]]
            mv = sp.Popen(comando)
        elif arquivo.endswith("stop"):
            stop.insert(0, arquivo)


criar_diretorios()
while stop[0] == "1":
    listar_arquivos()
    mover_arquivos()
    sleep(1)
