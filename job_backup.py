import zipfile, os, datetime

# Alterar as duas variáveis abaixo
nomeProjeto = 'Noma'
origem = 'F:\\teste'



###############################################################################################################################################

# FUNÇÃO QUE FAZ O BACKUP
def backupJob(folder):
    # VARIAVEIS DE NOMENCLATURA DE ARQUIVO
    aux = datetime.datetime.now()
    data = (str(aux.day) + '.' + str(aux.month) + '.' + str(aux.year))
    arquivoZip = 'Job_'+ nomeProjeto +'_' + data + '.zip'

    # Criação do arquivo com o nome personalizado
    print('Criando o arquivo %s...' % (arquivoZip))
    print('Isso pode demorar alguns segundos...')
    backupZip = zipfile.ZipFile(arquivoZip, 'w')

    # Loop de pastas, subpastas e arquivos no caminho de origem
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adicionando arquivos em %s...' % (foldername))

        # Adiciona os diretórios da pasta no zip
        backupZip.write(foldername)

        # Loop fazendo a busca em todos os arquivos e preenchendo no zip
        for filename in filenames:
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Backup feito com sucesso!.')

# CHAMADA DA FUNÇÃO COM O CAMINHO DE ORIGEM
backupJob(origem)      