# Meu Projeto Django
Bem-vindo ao Meu Projeto Django! Este é um projeto inicial para começar a desenvolver um aplicativo da web usando o framework Django.


# Configuração do Ambiente
Certifique-se de ter o Python instalado em sua máquina.

# Instale um ambiente virtual para evitar que o projeto seja instalado global em sua máquina.
Em Windows:

python -m venv virtual-env  
virtual-env\Scripts\activate.bat

Em Linux:

python -m venv virtual-env  
. venv/bin/activate

# Instale o Django
pip install django

"Esse passo pode ser ignorado caso queira utilizar o Django na versão da data. Instalando com o comando abaixo junto com as dependências necessárias."

# Instale as dependências do projeto (recomenda-se usar um ambiente virtual)
pip install -r requirements.txt

# Faça a migração do banco de dados
python manage.py migrate