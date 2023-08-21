"""
Ambientes virtuais em Python (venv)
Um ambiente virtual carrega toda a sua instalação do Python
para uma pasta no caminho escolhido.
Ao ativar um ambiente virtual, a instalação do ambiente virtual será usada.
venv é um módulo que vamos usar para criar ambientes virtuais.
Pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são:
venv    env     .venv    .env

Como criar ambientes virtuais:
Abra a pasta do seu projeto no terminal e digite:
python -m venv venv

Comandos:
venv\\Scripts\activate  - ativa o ambiente virtual
deactivate  - desativa o ambiente virtual
pip freeze  - mostra os pacotes instalados no ambiente virtual
pip freeze > requirements.txt  - cria um arquivo com os pacotes instalados
pip install -r requirements.txt (instala os pacotes
do arquivo requirements.txt)
pip install -U pip - atualiza o pip
pip install -U nome_do_pacote - atualiza o pacote
pip install -U -r requirements.txt - atualiza todos os pacotes
pip uninstall nome_do_pacote -y - desinstala o pacote
"""
